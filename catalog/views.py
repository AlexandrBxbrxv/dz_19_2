from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView

from catalog.forms import ConsumableForm, ConsumableModeratorForm
from catalog.models import Consumable, Equipment, Version


def consumable_purchase_count(request, pk):
    """Увеличивает счетчик покупок товара модели расходный материал"""
    product = get_object_or_404(Consumable, pk=pk)
    product.purchases_count += 1
    product.save()

    return redirect(reverse(f'catalog:consumables'))


def popular_products(request):
    """Выводит топ 3 наиболее покупаемых товаров модели расходный материал"""
    consumables = Consumable.objects.order_by('-purchases_count')[:3]
    return consumables


# Страницы без CRUD #####################################
class HomeTemplateView(TemplateView):
    template_name = 'catalog/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Главная', 'popular_products': popular_products(self.request)})
        return context


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Контакты'})
        return context


# система CRUD для модели Расходный материал ########################################
class ConsumableCreateView(CreateView):
    model = Consumable
    form_class = ConsumableForm
    success_url = reverse_lazy('catalog:consumables')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.creator = user
        product.save()
        return super().form_valid(form)


class ConsumablesListView(ListView):
    model = Consumable

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Расходники'})
        return context


class ConsumableDetailView(DetailView):
    model = Consumable

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Подробности товара'})
        return context


class ConsumableUpdateView(LoginRequiredMixin, UpdateView):
    model = Consumable
    form_class = ConsumableForm
    success_url = reverse_lazy('catalog:consumables')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.creator:
            self.object.save()
            return self.object
        raise PermissionDenied

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ConsumableFormset = inlineformset_factory(Consumable, Version, form=ConsumableForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = ConsumableFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ConsumableFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

    def get_form_class(self):
        user = self.request.user
        if user == self.object.creator:
            return ConsumableForm
        if user.has_perms(['catalog.set_published', 'catalog.change_description', 'catalog.change_category']):
            return ConsumableModeratorForm
        else:
            raise PermissionDenied


class ConsumableDeleteView(DeleteView):
    model = Consumable
    success_url = reverse_lazy('catalog:consumables')


# система CRUD для модели Техника ########################################
class EquipmentListView(ListView):
    model = Equipment

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Техника'})
        return context


class EquipmentDetailView(DetailView):
    model = Equipment

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Подробности товара'})
        return context

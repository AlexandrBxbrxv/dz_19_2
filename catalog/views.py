from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView

from catalog.models import Consumable, Equipment


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
    fields = ('name', 'description', 'image', 'category', 'price', 'created_at', 'updated_at')
    success_url = reverse_lazy('catalog:consumables')


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


class ConsumableUpdateView(UpdateView):
    model = Consumable
    fields = ('name', 'description', 'image', 'category', 'price', 'created_at', 'updated_at')
    success_url = reverse_lazy('catalog:consumables')


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

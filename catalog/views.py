from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.models import Consumable, Equipment, Blog


def consumable_purchase_count(request, pk):
    product = get_object_or_404(Consumable, pk=pk)
    product.purchases_count += 1
    product.save()

    return redirect(reverse(f'catalog:consumables'))


def popular_products(request):
    popular_products = []
    consumables = Consumable.objects.order_by('-purchases_count')[:3]
    return consumables

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


class ConsumableCreateView(CreateView):
    model = Consumable
    fields = ('name', 'description', 'image', 'category', 'price', 'created_at', 'updated_at')
    success_url = reverse_lazy('catalog:consumables')


class ConsumableUpdateView(UpdateView):
    model = Consumable
    fields = ('name', 'description', 'image', 'category', 'price', 'created_at', 'updated_at')
    success_url = reverse_lazy('catalog:consumables')


class ConsumableDeleteView(DeleteView):
    model = Consumable
    success_url = reverse_lazy('catalog:consumables')


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


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        """Фильтр для вывода на страницу только опубликованных блогов"""
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Блоги'})
        return context


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        """Добавление просмотра после обновления страницы"""
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'title': 'Подробности блога'})
        return context


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'body', 'preview', 'created_at')
    success_url = reverse_lazy('catalog:blogs')

    def form_valid(self, form):
        """Создаёт человеко понятный URL"""
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'body', 'preview', 'created_at', 'is_published')
    success_url = reverse_lazy('catalog:blogs')

    def get_success_url(self):
        return reverse('catalog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('catalog:blogs')

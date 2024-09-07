from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from catalog.models import Consumable, Equipment, Blog


class HomeTemplateView(TemplateView):
    template_name = 'catalog/home.html'


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'


class ConsumablesListView(ListView):
    model = Consumable

    # if request.method == "POST":
    #     check_box_list = request.POST.getlist('consumables_check')
    #     search_field = request.POST.get('search_field')
    #     consumable_list = (consumable_list.filter(
    #         name__icontains=search_field,
    #         category__in=check_box_list))


class ConsumableDetailView(DetailView):
    model = Consumable


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

    # if request.method == "POST":
    #     check_box_list = request.POST.getlist('equipment_check')
    #     search_field = request.POST.get('search_field')
    #     equipment_list = (equipment_list.filter(
    #         name__icontains=search_field,
    #         category__in=check_box_list))


class EquipmentDetailView(DetailView):
    model = Equipment


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'body', 'preview', 'created_at')
    success_url = reverse_lazy('catalog:blogs')

    def form_valid(self, form):
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

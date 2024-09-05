from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView

from catalog.models import Consumable, Equipment


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


class EquipmentListView(ListView):
    model = Equipment

    # if request.method == "POST":
    #     check_box_list = request.POST.getlist('equipment_check')
    #     search_field = request.POST.get('search_field')
    #     equipment_list = (equipment_list.filter(
    #         name__icontains=search_field,
    #         category__in=check_box_list))


class ProductDetailView(DetailView):
    model = Consumable


class ConsumableCreateView(CreateView):
    model = Consumable
    fields = ('name', 'description', 'image', 'category', 'price', 'created_at', 'updated_at')
    success_url = reverse_lazy('catalog:consumable_list')


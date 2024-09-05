from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView

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


def add_product(request):
    context = {
        'page_name': 'Добавление продукта'
    }
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        category = request.POST.get('category')
        description = request.POST.get('description')
        image = request.POST.get('image')

    return render(request, 'catalog/add_product.html', context)

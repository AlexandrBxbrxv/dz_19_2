from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView

from catalog.models import Product


class HomeTemplateView(TemplateView):
    template_name = 'catalog/home.html'


class ContactsTemplateView(TemplateView):
    template_name = 'catalog/contacts.html'


class ConsumablesListView(ListView):
    model = Product

#     if request.method == "POST":
#         check_box_list = request.POST.getlist('consumables_check')
#         search_field = request.POST.get('search_field')
#         consumable_list = (consumable_list.filter(
#             name__icontains=search_field,
#             category__in=check_box_list))


def equipment(request):
    equipment_list = Product.objects.filter(category__in=[5, 31])  # Только категория принтеры
    if request.method == "POST":
        check_box_list = request.POST.getlist('equipment_check')
        search_field = request.POST.get('search_field')
        equipment_list = (equipment_list.filter(
            name__icontains=search_field,
            category__in=check_box_list))

    context = {
        'equipment': equipment_list,
        'page_name': 'Техника'
    }
    return render(request, 'catalog/equipment.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product,
        'page_name': 'Страница товара'
    }
    return render(request, 'catalog/product_detail.html', context)


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

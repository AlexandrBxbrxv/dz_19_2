from django.shortcuts import render

from catalog.models import Product


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == "POST":
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        user_message = request.POST.get('user_message')
        print(user_name, user_email, user_message)
    return render(request, 'catalog/contacts.html')


def consumables(request):
    consumable_list = Product.objects.exclude(category=5)  # Исключая категорию принтеры
    context = {
        'consumables': consumable_list,
        'page_name': ''
    }
    return render(request, 'catalog/consumables.html', context)


def equipment(request):
    equipment_list = Product.objects.filter(category=5)  # только категория принтеры
    context = {
        'equipment': equipment_list,
        'page_name': ''
    }
    return render(request, 'catalog/equipment.html', context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product,
        'page_name': 'Страница товара'
    }
    return render(request, 'catalog/product_detail.html', context)


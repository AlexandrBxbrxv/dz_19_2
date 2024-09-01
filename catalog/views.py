from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    context = {
        'page_name': 'Главная'
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    context = {
        'page_name': 'Контакты'
    }
    if request.method == "POST":
        user_name = request.POST.get('user_name')
        user_email = request.POST.get('user_email')
        user_message = request.POST.get('user_message')
        print(user_name, user_email, user_message)
    return render(request, 'catalog/contacts.html', context)


def consumables(request):
    consumable_list = Product.objects.exclude(category=5)  # Исключая категорию принтеры
    if request.method == "POST":
        check_box_list = request.POST.getlist('consumables_check')
        search_field = request.POST.get('search_field')
        consumable_list = Product.objects.exclude(category=5).filter(name__icontains=search_field, category__in=check_box_list)

    context = {
        'consumables': consumable_list,
        'page_name': 'Расходники'
    }
    return render(request, 'catalog/consumables.html', context)


def equipment(request):
    equipment_list = Product.objects.filter(category=5)  # только категория принтеры
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


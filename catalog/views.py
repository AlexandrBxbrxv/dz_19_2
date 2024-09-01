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


def store(request):
    consumables = Product.objects.exclude(category=5)  # Исключая категорию принтеры
    context = {'consumables': consumables}
    return render(request, 'catalog/store.html', context)

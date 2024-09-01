from django.core.management import BaseCommand
import json

from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('fixtures/catalog_data_2.json', 'r', encoding='utf-8') as file:
            dict_list = json.loads(file.read())
            # Сначала должны создаваться модели класса Категория, без них не смогут создаться модели класса Продукт
            categories = []
            products = []
        for item in dict_list:
            if item['model'] == 'catalog.category':
                categories.append(item)
            else:
                products.append(item)

        Product.objects.all().delete()
        Category.objects.all().delete()

        categories_for_create = []
        for category in categories:
            fields = category['fields']
            categories_for_create.append(Category(
                pk=category['pk'],
                name=fields['name'],
                description=fields['description']
            ))
        Category.objects.bulk_create(categories_for_create)

        products_for_create = []
        for product in products:
            fields = product['fields']
            products_for_create.append(Product(
                pk=product['pk'],
                name=fields['name'],
                description=fields['description'],
                image=fields['image'],
                category=Category.objects.get(pk=fields['category']),
                price=fields['price'],
                created_at=fields['created_at'],
                updated_at=fields['updated_at']
                ))

        Product.objects.bulk_create(products_for_create)





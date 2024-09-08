from django.core.management import BaseCommand
import json

from catalog.models import Category, Consumable, Equipment, Blog


class Command(BaseCommand):
    """Команда для заполнения базы данных"""
    def handle(self, *args, **options):
        with open('fixtures/catalog_data.json', 'r', encoding='utf-8') as file:
            dict_list = json.loads(file.read())

# сортировка
            categories = []
            consumables = []
            equipments = []
            blogs = []

        for item in dict_list:
            if item['model'] == 'catalog.category':
                categories.append(item)
            elif item['model'] == 'catalog.consumable':
                consumables.append(item)
            elif item['model'] == 'catalog.equipment':
                equipments.append(item)
            elif item['model'] == 'catalog.blog':
                blogs.append(item)

# отчистка базы данных
        Consumable.objects.all().delete()
        Equipment.objects.all().delete()
        Blog.objects.all().delete()
        Category.objects.all().delete()

# создание объектов модели КАТЕГОРИЯ
        categories_for_create = []
        for item in categories:
            fields = item['fields']
            categories_for_create.append(Category(
                pk=item['pk'],
                name=fields['name'],
                description=fields['description']
            ))
        Category.objects.bulk_create(categories_for_create)

# создание объектов модели РАСХОДНЫЙ МАТЕРИАЛ
        consumables_for_create = []
        for item in consumables:
            fields = item['fields']
            consumables_for_create.append(Consumable(
                pk=item['pk'],
                name=fields['name'],
                description=fields['description'],
                image=fields['image'],
                category=Category.objects.get(pk=fields['category']),
                price=fields['price'],
                created_at=fields['created_at'],
                updated_at=fields['updated_at']
                ))
        Consumable.objects.bulk_create(consumables_for_create)

# создание объектов модели ТЕХНИКА
        equipments_for_create = []
        for item in equipments:
            fields = item['fields']
            equipments_for_create.append(Equipment(
                pk=item['pk'],
                name=fields['name'],
                description=fields['description'],
                image=fields['image'],
                category=Category.objects.get(pk=fields['category']),
                price=fields['price'],
                guarantee=fields['guarantee'],
                manufacturer=fields['manufacturer'],
                created_at=fields['created_at'],
                updated_at=fields['updated_at']
            ))
        Equipment.objects.bulk_create(equipments_for_create)

# создание объектов модели БЛОГ
        blogs_for_create = []
        for item in blogs:
            fields = item['fields']
            blogs_for_create.append(Blog(
                pk=item['pk'],
                title=fields['title'],
                slug=fields['slug'],
                body=fields['body'],
                preview=fields['preview'],
                is_published=fields['is_published'],
                views_count=fields['views_count'],
                created_at=fields['created_at']
            ))
        Blog.objects.bulk_create(blogs_for_create)





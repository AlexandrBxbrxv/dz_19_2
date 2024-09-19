from django.core.management import BaseCommand
import json

from catalog.models import Category, Consumable, Equipment, Version
from blog.models import Blog


class Command(BaseCommand):
    """Команда для заполнения базы данных"""
    def handle(self, *args, **options):

        all_fixtures = []

        with open('fixtures/catalog_data.json', 'r', encoding='utf-8') as file:
            all_fixtures.extend(json.loads(file.read()))

        with open('fixtures/blog_data.json', 'r', encoding='utf-8') as file:
            all_fixtures.extend(json.loads(file.read()))

# сортировка
            categories = []
            consumables = []
            versions = []
            equipments = []
            blogs = []

        for item in all_fixtures:
            if item['model'] == 'catalog.category':
                categories.append(item)
            elif item['model'] == 'catalog.consumable':
                consumables.append(item)
            elif item['model'] == 'catalog.version':
                versions.append(item)
            elif item['model'] == 'catalog.equipment':
                equipments.append(item)
            elif item['model'] == 'blog.blog':
                blogs.append(item)

# отчистка базы данных
        Version.objects.all().delete()
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
                purchases_count=fields['purchases_count'],
                created_at=fields['created_at'],
                updated_at=fields['updated_at']
            ))
        Consumable.objects.bulk_create(consumables_for_create)

# создание объектов модели ВЕРСИЯ для расходных материалов
        versions_for_create = []
        for item in versions:
            fields = item['fields']
            versions_for_create.append(Version(
                pk=item['pk'],
                name=fields['name'],
                number=fields['number'],
                consumable_product=Consumable.objects.get(pk=fields['consumable_product']),
                is_current_version=fields['is_current_version']
            ))
        Version.objects.bulk_create(versions_for_create)

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
                purchases_count=fields['purchases_count'],
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

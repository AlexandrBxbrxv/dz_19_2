from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('fixtures/catalog_data.json', 'r', encoding='utf-8') as file:
            data = file.read()
        print(data)

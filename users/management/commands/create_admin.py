import os

from django.core.management import BaseCommand
from users.models import User
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env')


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@bk.ru',
            first_name='Alexander',
            last_name='Bobrov',
            is_staff=True,
            is_superuser=True
        )

        user.set_password(os.getenv('ADMIN_PASSWORD'))
        user.save()

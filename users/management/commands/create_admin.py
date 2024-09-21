from django.core.management import BaseCommand

from users.models import User

from func_get_password import get_password


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@bk.ru',
            first_name='Alexander',
            last_name='Bobrov',
            is_staff=True,
            is_superuser=True
        )

        user.set_password(get_password('admin_password.txt'))
        user.save()

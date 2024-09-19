from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    phone = models.CharField(max_length=35, **NULLABLE, verbose_name='телефон')
    avatar = models.ImageField(upload_to='users/avatars', **NULLABLE, verbose_name='аватар')
    country = models.CharField(max_length=100, verbose_name='страна')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

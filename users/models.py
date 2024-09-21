from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    phone = models.CharField(max_length=35, **NULLABLE, verbose_name='телефон')
    avatar = models.ImageField(upload_to='users/avatars', **NULLABLE, verbose_name='аватар')
    country = models.CharField(max_length=100, verbose_name='страна')

    token = models.CharField(max_length=100, **NULLABLE, verbose_name='token')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

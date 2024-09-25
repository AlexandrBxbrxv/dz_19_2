from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Consumable(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(**NULLABLE, verbose_name='описание')
    image = models.ImageField(**NULLABLE, upload_to='consumable/images', verbose_name='изображение')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='категория',
                                 **NULLABLE)
    price = models.IntegerField(verbose_name='цена')
    purchases_count = models.IntegerField(default=0, verbose_name='единиц куплено')
    created_at = models.DateField(**NULLABLE, verbose_name='дата создания')
    updated_at = models.DateField(**NULLABLE, verbose_name='дата последнего изменения')

    creator = models.ForeignKey(User, related_name='creator', on_delete=models.SET_NULL,
                                **NULLABLE, verbose_name='создатель')
    is_published = models.BooleanField(default=False, verbose_name='признак публикации')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        permissions = [
            ('set_published', 'Can set publication status of product'),
            ('change_description', 'Can change description of product'),
            ('change_category', 'Can change category of product')
        ]

        verbose_name = 'расходный материал'
        verbose_name_plural = 'расходные материалы'
        ordering = ('price', 'purchases_count',)


class Equipment(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    guarantee = models.CharField(max_length=100, verbose_name='гарантия')
    manufacturer = models.CharField(max_length=200, verbose_name='производитель')
    description = models.TextField(**NULLABLE, verbose_name='описание')
    image = models.ImageField(**NULLABLE, upload_to='equipment/images', verbose_name='изображение')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='категория',
                                 **NULLABLE)
    price = models.IntegerField(verbose_name='цена')
    purchases_count = models.IntegerField(default=0, verbose_name='единиц куплено')
    created_at = models.DateField(**NULLABLE, verbose_name='дата создания')
    updated_at = models.DateField(**NULLABLE, verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'техника'
        verbose_name_plural = 'техника'
        ordering = ('price', 'purchases_count',)


class Version(models.Model):
    consumable_product = models.ForeignKey(Consumable, related_name='consumable_versions', on_delete=models.SET_NULL,
                                           verbose_name='версии продукта расходника', **NULLABLE)
    number = models.PositiveIntegerField(default=1, verbose_name='номер версии')
    name = models.CharField(max_length=150, verbose_name='название версии')
    is_current_version = models.BooleanField(default=True, verbose_name='активность версии')

    def __str__(self):
        return f'{self.name}, №{self.number}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
        ordering = ('number', 'name',)

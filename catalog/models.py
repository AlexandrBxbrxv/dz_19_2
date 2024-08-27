from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(**NULLABLE, verbose_name='описание')
    image = models.ImageField(**NULLABLE, upload_to='product_images/', verbose_name='изображение')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='категория',
                                 **NULLABLE, related_name='categories')
    price = models.IntegerField(verbose_name='цена')
    created_at = models.DateField(**NULLABLE, verbose_name='дата создания')
    updated_at = models.DateField(**NULLABLE, verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('price',)

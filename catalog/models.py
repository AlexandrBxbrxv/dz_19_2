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


class Consumable(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    description = models.TextField(**NULLABLE, verbose_name='описание')
    image = models.ImageField(**NULLABLE, upload_to='consumable/images', verbose_name='изображение')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='категория',
                                 **NULLABLE)
    price = models.IntegerField(verbose_name='цена')
    created_at = models.DateField(**NULLABLE, verbose_name='дата создания')
    updated_at = models.DateField(**NULLABLE, verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'расходный материал'
        verbose_name_plural = 'расходные материалы'
        ordering = ('price',)


class Equipment(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    guarantee = models.IntegerField(default=0, verbose_name='гарантия')
    manufacturer = models.CharField(max_length=200, verbose_name='производитель')
    description = models.TextField(**NULLABLE, verbose_name='описание')
    image = models.ImageField(**NULLABLE, upload_to='equipment/images', verbose_name='изображение')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='категория',
                                 **NULLABLE)
    price = models.IntegerField(verbose_name='цена')
    created_at = models.DateField(**NULLABLE, verbose_name='дата создания')
    updated_at = models.DateField(**NULLABLE, verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'техника'
        verbose_name_plural = 'техника'
        ordering = ('price',)


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    body = models.TextField(verbose_name='контент')
    preview = models.ImageField(upload_to='blog/image', verbose_name='превью', **NULLABLE)
    created_at = models.DateField(**NULLABLE, verbose_name='дата создания')
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    views_count = models.IntegerField(default=0, verbose_name='количество просмотров')

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'

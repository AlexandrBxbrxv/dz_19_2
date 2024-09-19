from django.db import models

NULLABLE = {'blank': True, 'null': True}


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

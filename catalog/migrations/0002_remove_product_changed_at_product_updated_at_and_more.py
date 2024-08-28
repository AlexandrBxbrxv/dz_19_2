# Generated by Django 5.1 on 2024-08-27 19:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='changed_at',
        ),
        migrations.AddField(
            model_name='product',
            name='updated_at',
            field=models.DateField(blank=True, null=True, verbose_name='дата последнего изменения'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categories', to='catalog.category', verbose_name='категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateField(blank=True, null=True, verbose_name='дата создания'),
        ),
    ]

# Generated by Django 5.1 on 2024-09-05 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_consumable_category_equipment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='equipment/images', verbose_name='изображение'),
        ),
    ]

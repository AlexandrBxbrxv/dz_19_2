from django.contrib import admin
from catalog.models import Category, Consumable, Equipment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Consumable)
class ConsumableAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'purchases_count')
    list_filter = ('category',)
    search_fields = ('name',)


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'guarantee', 'purchases_count')
    list_filter = ('category',)
    search_fields = ('name',)

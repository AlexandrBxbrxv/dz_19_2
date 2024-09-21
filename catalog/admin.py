from django.contrib import admin
from catalog.models import Category, Consumable, Equipment, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Consumable)
class ConsumableAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'purchases_count', 'creator')
    list_filter = ('category', 'creator')
    search_fields = ('name',)


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'guarantee', 'purchases_count')
    list_filter = ('category',)
    search_fields = ('name',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'consumable_product', 'number', 'name', 'is_current_version')
    list_filter = ('is_current_version',)
    search_fields = ('name',)


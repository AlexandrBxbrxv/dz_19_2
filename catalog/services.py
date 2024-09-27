from django.core.cache import cache

from catalog.models import Consumable
from config.settings import CACHE_ENABLED


def get_consumables_from_cache():
    """Возвращает из кеша список consumables, если кеш пуст записывает этот список в кеш"""
    if not CACHE_ENABLED:
        return Consumable.objects.all()
    key = 'consumable_list'
    consumables = cache.get(key)
    if consumables is not None:
        return consumables
    cache.set(key, Consumable.objects.all())

from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, consumables, equipment

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts', contacts, name='contacts'),
    path('consumables', consumables, name='consumables'),
    path('equipment', equipment, name='equipment'),

]

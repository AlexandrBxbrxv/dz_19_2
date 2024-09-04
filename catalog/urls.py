from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, equipment, product_detail, add_product, ConsumablesListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts', contacts, name='contacts'),
    path('consumables', ConsumablesListView.as_view(), name='consumables'),
    path('equipment', equipment, name='equipment'),
    path('product_detail/<int:pk>/', product_detail, name='product_detail'),
    path('add_product', add_product, name='add_product'),
]

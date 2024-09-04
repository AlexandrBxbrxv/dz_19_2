from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import HomeTemplateView, equipment, ProductDetailView, add_product, ConsumablesListView, ContactsTemplateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('contacts', ContactsTemplateView.as_view(), name='contacts'),
    path('consumables', ConsumablesListView.as_view(), name='consumables'),
    path('equipment', equipment, name='equipment'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('add_product', add_product, name='add_product'),
]

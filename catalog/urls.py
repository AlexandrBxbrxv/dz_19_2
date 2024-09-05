from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import HomeTemplateView, ProductDetailView, ConsumablesListView, ContactsTemplateView, \
    EquipmentListView, ConsumableCreateView, ConsumableUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('contacts', ContactsTemplateView.as_view(), name='contacts'),
    path('consumables', ConsumablesListView.as_view(), name='consumables'),
    path('equipment', EquipmentListView.as_view(), name='equipment'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('consumable/create', ConsumableCreateView.as_view(), name='consumable_create'),
    path('consumable/<int:pk>/update', ConsumableUpdateView.as_view(), name='consumable_update'),
]

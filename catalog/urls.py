from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import HomeTemplateView, ConsumableDetailView, ConsumablesListView, ContactsTemplateView, \
    EquipmentListView, ConsumableCreateView, ConsumableUpdateView, ConsumableDeleteView, EquipmentDetailView, \
    consumable_purchase_count

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),

    path('consumable/create/', ConsumableCreateView.as_view(), name='consumable_create'),
    path('consumables/', ConsumablesListView.as_view(), name='consumables'),
    path('consumable/detail/<int:pk>/', cache_page(60)(ConsumableDetailView.as_view()), name='consumable_detail'),
    path('consumable/update/<int:pk>/', ConsumableUpdateView.as_view(), name='consumable_update'),
    path('consumable/delete/<int:pk>/', ConsumableDeleteView.as_view(), name='consumable_delete'),
    path('consumable/purchase/<int:pk>/', consumable_purchase_count, name='consumable_purchase'),
    path('equipments/', EquipmentListView.as_view(), name='equipments'),
    path('equipment/detail/<int:pk>/', EquipmentDetailView.as_view(), name='equipment_detail'),
]

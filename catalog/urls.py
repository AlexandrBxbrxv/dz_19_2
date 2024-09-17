from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import HomeTemplateView, ConsumableDetailView, ConsumablesListView, ContactsTemplateView, \
    EquipmentListView, ConsumableCreateView, ConsumableUpdateView, ConsumableDeleteView, EquipmentDetailView, \
    consumable_purchase_count

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('contacts', ContactsTemplateView.as_view(), name='contacts'),
    path('consumables', ConsumablesListView.as_view(), name='consumables'),
    path('equipments', EquipmentListView.as_view(), name='equipments'),
    path('equipment/detail/<int:pk>/', EquipmentDetailView.as_view(), name='equipment_detail'),
    path('consumable/detail/<int:pk>/', ConsumableDetailView.as_view(), name='consumable_detail'),
    path('consumable/create', ConsumableCreateView.as_view(), name='consumable_create'),
    path('consumable/<int:pk>/update', ConsumableUpdateView.as_view(), name='consumable_update'),
    path('consumable/<int:pk>/delete', ConsumableDeleteView.as_view(), name='consumable_delete'),
    path('consumable/<int:pk>/purchase', consumable_purchase_count, name='consumable_purchase'),
]

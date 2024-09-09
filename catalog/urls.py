from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import HomeTemplateView, ConsumableDetailView, ConsumablesListView, ContactsTemplateView, \
    EquipmentListView, ConsumableCreateView, ConsumableUpdateView, BlogListView, BlogDetailView, BlogCreateView, \
    BlogUpdateView, ConsumableDeleteView, EquipmentDetailView, BlogDeleteView, consumable_purchase_count

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
    path('blogs', BlogListView.as_view(), name='blogs'),
    path('blog/<int:pk>/detail', BlogDetailView.as_view(), name='blog_detail'),
    path('blog/create', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/update', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete', BlogDeleteView.as_view(), name='blog_delete'),
    path('consumable/<int:pk>/purchase', consumable_purchase_count, name='consumable_purchase'),
]

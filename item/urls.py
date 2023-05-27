from django.urls import path
from .views import item_home, save_item, list_items, update_item, update, delete_item, search_items
app_name = 'items'
urlpatterns = [
    path('', item_home),
    path('salvar/', save_item, name="salvar"),
    path('items/', list_items, name="items"),
    path('editar/<int:id>/', update_item, name="editar"),
    path('update/<int:id>/', update, name="update"),
    path('delete/<int:id>/', delete_item, name="delete"),
    path('search/', search_items, name="search"),
]

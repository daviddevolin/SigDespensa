from django.contrib import admin
from django.urls import path, include
from .views import home, save_category, list_categories, update_category, update, delete_category,search_categories
app_name = 'categories'
urlpatterns =  [
    path('', home,name= "home"),
    path('salvar/', save_category, name="salvar"),
    path('categories/', list_categories, name="categories"),
    path('editar/<int:id>', update_category, name="editar"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete_category, name="delete"),
    path('search/', search_categories, name="search")
]

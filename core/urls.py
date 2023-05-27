from django.contrib import admin
from django.urls import path, include
from .views import home, save_user, list_users, update_user, update, delete_user, search_users
app_name = 'users'
urlpatterns =  [
    path('', home),
    path('salvar/', save_user, name="salvar"),
    path('users/', list_users, name="users"),
    path('editar/<int:id>', update_user, name="editar"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete_user, name="delete"),
    path('search/', search_users, name="search")
]

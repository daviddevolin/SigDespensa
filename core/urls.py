from django.contrib import admin
from django.urls import path, include
from .views import home, saveUser, listUsers, updateUser, update, deleteUser
urlpatterns = [
    path('', home),
    path('salvar/', saveUser, name="salvar"),
    path('users/', listUsers, name="users"),
    path('editar/<int:id>', updateUser, name="editar"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', deleteUser, name="delete")
]

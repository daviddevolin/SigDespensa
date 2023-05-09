from django.contrib import admin
from django.urls import path, include
from .views import home, saveUser, listUsers
urlpatterns = [
    path('', home),
    path('salvar/', saveUser, name="salvar"),
    path('users/', listUsers, name="users"),
]

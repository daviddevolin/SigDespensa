from django.urls import path
from .views import (
    despensa_list,
    despensa_detail,
    despensa_create,
    despensa_update,
    despensa_delete
)
app_name='despensas'

urlpatterns = [
    path('', despensa_list, name='despensa_list'),
    path('<int:pk>', despensa_detail, name='despensa_detail'),
    path('create/', despensa_create, name='despensa_create'),
    path('update/<int:pk>', despensa_update, name='despensa_update'),
    path('delete/<int:pk>', despensa_delete, name='despensa_delete'),
]

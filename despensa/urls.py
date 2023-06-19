from django.urls import path
from .views import (
    despensa_list,
    despensa_detail,
    despensa_create,
    despensa_update,
    despensa_delete,
    despensa_form,
    update
)
app_name='despensas'

urlpatterns = [
    path('', despensa_list, name='despensa_list'),
    path('form/', despensa_form, name="despensa_form"),
    path('<int:id>', despensa_detail, name='despensa_detail'),
    path('create/', despensa_create, name='despensa_create'),
    path('editar/<int:id>', despensa_update, name='despensa_update'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', despensa_delete, name='despensa_delete'),
]

from django.urls import path
from despensa.views import (
    despensa_list,
    despensa_detail,
    despensa_create,
    despensa_update,
    despensa_delete
)

urlpatterns = [
    path('', despensa_list, name='despensa_list'),
    path('<int:pk>/', despensa_detail, name='despensa_detail'),
    path('create/', despensa_create, name='despensa_create'),
    path('<int:pk>/update/', despensa_update, name='despensa_update'),
    path('<int:pk>/delete/', despensa_delete, name='despensa_delete'),
]

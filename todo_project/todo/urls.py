from django.urls import path
from . import views  

urlpatterns = [
    path('', views.list_todo_items, name='listitems'),
    path('update-items/<str:pk>/',views.update_todo_items,name= 'update-items') ,
    path('delete-items/<str:pk>/',views.delete_todo_items,name= 'delete-items')
]

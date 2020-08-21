from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_todo_items),
    path('insert_todo_item', views.insert_todo_item, nam='insert')
]

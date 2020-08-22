
from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_form), # Localhost/employee/list
    path('list/', views.employee_list),
]

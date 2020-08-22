
from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_form, name="employee_insert"), # get and post request for inser
    path('<int:id>/', views.employee_form, name="employee_update"), # get and post requesst for update
    path('list/', views.employee_list, name="employee_list"), # this is for retrive and display records
    path('delete/<int:id>', views.employee_delete, name="employee_delete"),
]

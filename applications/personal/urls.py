from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('list-all-empleados', views.ListAllEmpleados.as_view()),
    path('list-area', views.ListByAreaEmpleados.as_view()),
]

from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('list-all-empleados/', views.ListAllEmpleados.as_view()),
    path('list-area/<shortName>/', views.ListByAreaEmpleados.as_view()),
    path('buscar-emp/', views.ListEmpleadosByKword.as_view()),
]

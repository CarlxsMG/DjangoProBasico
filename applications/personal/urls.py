from django.contrib import admin
from django.urls import path

from . import views

# nombre para el conjungto de estas urls
app_name = 'personal_app'

urlpatterns = [
    path('list-all-empleados/', views.ListAllEmpleados.as_view()),
    path('list-area/<shortName>/', views.ListByAreaEmpleados.as_view()),
    path('buscar-emp/', views.ListEmpleadosByKword.as_view()),
    path('listar-habilidades/', views.ListHabilidadesEmplead.as_view()),
    path('ver-empleado/<pk>', views.EmpleadoDetailView.as_view()),
    path('add-empleado/', views.EmpleadoCreateView.as_view()),
    path('success/', views.SuccessView.as_view(), name='added'),
]

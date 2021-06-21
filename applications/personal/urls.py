from django.contrib import admin
from django.urls import path

from . import views

# nombre para el conjungto de estas urls
app_name = 'personal_app'

urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),
    path('list-all-empleados/', views.ListAllEmpleados.as_view(), name='empleados_all'),
    path('lista-empleados-admin/', views.ListaEmpleadosAdmin.as_view(), name='empleados_admin'),
    path('list-area/<shortName>/', views.ListByAreaEmpleados.as_view(), name='empleadosArea'),
    path('buscar-emp/', views.ListEmpleadosByKword.as_view()),
    path('listar-habilidades/', views.ListHabilidadesEmplead.as_view()),
    path('ver-empleado/<pk>', views.EmpleadoDetailView.as_view(), name='empleado_detail'),
    path('add-empleado/', views.EmpleadoCreateView.as_view(), name='empleado_add'),
    path('success/', views.SuccessView.as_view(), name='added'),
    path('update-empleado/<pk>', views.EmpleadoUpdateView.as_view(), name='modificar'),
    path('delete-empleado/<pk>', views.EmpleadoDeleteView.as_view(), name='borrar'),
]

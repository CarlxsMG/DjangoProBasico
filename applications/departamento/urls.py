from django import forms
from django.contrib import admin
from django.urls import path

from . import views

# nombre para el conjungto de estas urls
app_name = 'departamento_app'


urlpatterns = [
    path('new-departamento/', views.NewDepartamentoView.as_view(), name='nuevoDepartamento'),
    path('lista-departamento/', views.DepartamentoListView.as_view(), name='listaDepartamento'),
]

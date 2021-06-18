from applications.home.models import HomeP
from django.shortcuts import render

# Import models
from .models import HomeP

# Plantillas genericas html
from django.views.generic import (
    TemplateView, 
    ListView, 
    CreateView)

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/home.html'

class HomeListView(ListView):
    template_name = "home/home_list.html"
    context_object_name = 'listNum'
    queryset = ['0','10','20','30']

class HomeListPrueba(ListView):
    template_name = "home/home_list_prueba.html"
    model = HomeP
    context_object_name = "listHome"
    
class HomeCreateView(CreateView):
    model = HomeP
    template_name = "home/home_add.html"
    fields = ['titulo', 'subtitulo', 'cantidad']

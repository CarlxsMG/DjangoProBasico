from django.shortcuts import render

# Plantillas genericas html
from django.views.generic import TemplateView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/home.html'
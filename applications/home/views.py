from django.shortcuts import render

# Plantillas genericas html
from django.views.generic import TemplateView, ListView

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/home.html'

class HomeListView(ListView):
    template_name = "home/home_list.html"
    context_object_name = 'listNum'
    queryset = ['0','10','20','30']
    

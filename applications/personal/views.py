from django.shortcuts import render

from .models import employed

# Plantillas genericas html
from django.views.generic import (
    ListView
    )

# Create your views here.
class ListAllEmpleados(ListView):
    template_name = 'personal/list_all.html'
    model = employed

class ListByAreaEmpleados(ListView):
    template_name = 'personal/list_area.html'
    queryset = employed.objects.filter(
        departamento__shortName='Direccion'
    )

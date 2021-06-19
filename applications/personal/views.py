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
    context_object_name = 'lista'

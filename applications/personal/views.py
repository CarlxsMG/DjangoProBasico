from django.shortcuts import render

from .models import employed

# Plantillas genericas html
from django.views.generic import (
    ListView
    )

# Create your views here.
class ListAllEmpleados(ListView):
    template_name = 'personal/list_all.html'
    paginate_by = 2
    ordering = 'first_name'
    model = employed

class ListByAreaEmpleados(ListView):
    template_name = 'personal/list_area.html'
    

    def get_queryset(self):
        #Devuelve una lista
        area = self.kwargs['shortName']
        queryset = employed.objects.filter(
            departamento__shortName=area
        )
        return queryset

class ListEmpleadosByKword(ListView):
    ''' lista empleado por palabra clave '''
    template_name = 'personal/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        clave = self.request.GET.get('kword',)

        queryset = employed.objects.filter(
            first_name=clave,
        )

        return queryset

class ListHabilidadesEmplead(ListView):
    template_name = 'personal/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = employed.objects.get(id=3)
        
        return empleado.habilidades.all()
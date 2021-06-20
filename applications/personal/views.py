from django.shortcuts import render

from django.urls import reverse_lazy

from django.views.generic.base import TemplateView

from .models import employed

# Plantillas genericas html
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView
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

class EmpleadoDetailView(DetailView):
    model = employed
    template_name = 'personal/detail_emp.html'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context

class SuccessView(TemplateView):
    template_name = 'personal/success.html'

class EmpleadoCreateView(CreateView):
    model = employed
    template_name = 'personal/add.html'

    fields = ['first_name','last_name','job','departamento','habilidades',]
    #fields = ('__all__')
    success_url = reverse_lazy('personal_app:added')

    def form_valid(self, form):

        empleado = form.save()
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()

        return super(EmpleadoCreateView, self).form_valid(form)
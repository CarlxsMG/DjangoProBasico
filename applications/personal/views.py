from django.db import models
from django.shortcuts import render

from django.urls import reverse_lazy

# models
from .models import employed

# forms
from .forms import EmpleadoForm

# Plantillas genericas html
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    TemplateView,
    DeleteView
    )

class InicioView(TemplateView):
    template_name = 'home/inicio.html'

# Create your views here.
class ListAllEmpleados(ListView):
    template_name = 'personal/list_all.html'
    paginate_by = 2
    ordering = 'first_name'
    context_object_name = 'empleados_to'

    def get_queryset(self):
        #Devuelve una lista
        clave = self.request.GET.get('kword', '')
        queryset = employed.objects.filter(
            first_name__icontains=clave,
        )
        return queryset

class ListByAreaEmpleados(ListView):
    template_name = 'personal/list_area.html'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        #Devuelve una lista
        area = self.kwargs['shortName']
        queryset = employed.objects.filter(
            departamento__shortName=area
        )
        return queryset

class ListaEmpleadosAdmin(ListView):
    template_name = 'personal/lista_empleados.html'
    paginate_by = 6
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = employed


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

    form_class = EmpleadoForm
    #fields = ['first_name','last_name','job','departamento','habilidades','image',]
    #fields = ('__all__')
    success_url = reverse_lazy('personal_app:empleados_admin')

    def form_valid(self, form):

        empleado = form.save(commit=False) #commit para ahorrarse el guardado antes de la modificacion (optimizacion codigo)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()

        return super(EmpleadoCreateView, self).form_valid(form)

class EmpleadoUpdateView(UpdateView):
    model = employed
    template_name = 'personal/update.html'

    fields = ['first_name','last_name','job','departamento','habilidades','image',]

    success_url = reverse_lazy('personal_app:empleados_admin')

    def post(self, request, *args, **kwargs) :
        self.object = self.get_object()

        #print(request.POST)
        #print(request.POST['last_name'])

        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        return super(EmpleadoUpdateView, self).form_valid(form)

class EmpleadoDeleteView(DeleteView):
    model = employed
    template_name = 'personal/delete.html'

    success_url = reverse_lazy('personal_app:empleados_admin')
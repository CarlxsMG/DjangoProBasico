from django import forms
import django
from django.shortcuts import render

from django.views.generic import ListView
from django.views.generic.edit import FormView

from applications.personal.models import employed
from .models import departamento

from .forms import NewDepartamentoForm
# Create your views here.
class DepartamentoListView(ListView):
    template_name = 'departamento/lista.html'
    model = departamento
    context_object_name = 'departamentos'

class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):

        dep = departamento(
            name = form.cleaned_data['departamento'],
            shortName = form.cleaned_data['shorname'],
        )
        dep.save()

        
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']

        employed.objects.create(
            first_name=nombre,
            last_name=apellido,
            job='1',
            departamento=dep
        )

        return super(NewDepartamentoView, self).form_valid(form)
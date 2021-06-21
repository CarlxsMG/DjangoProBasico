from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import employed

class EmpleadoForm(forms.ModelForm):

    class Meta: 
        model = employed
        fields = (
            'first_name',
            'last_name',
            'job',
            'departamento',
            'image',
            'habilidades',
        )
        widgets = {
            'habilidades': forms.CheckboxSelectMultiple()
        }
from django import forms
from django.db import models
from django.forms import fields, widgets

from .models import HomeP

class PruebaForm(forms.ModelForm):

    class Meta:
        model = HomeP
        fields = (
            'titulo',
            'subtitulo',
            'cantidad',
        )

        widgets = {
            'titulo': forms.TextInput(
                attrs={
                    'placeholder':'Titulo',
                    'style':'background: #000000; color: #FFFFFF',
                    'class':'titulo'
                }
            ),
            'cantidad': forms.NumberInput(
                attrs={
                    'placeholder':'Cantidad',
                }
            )
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('Cantidad no valida, num > 10')

        return cantidad
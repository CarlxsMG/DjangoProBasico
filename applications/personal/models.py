from django.db import models

# import CKEditor
from ckeditor.fields import RichTextField

# import to foreignkey
from applications.departamento.models import departamento

class Habilidades(models.Model):
    ''' Habilidades de los empleados '''
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades empleados'

    def __str__(self):
        return str(self.id)+ ' - ' + self.habilidad

# Create your models here.
class employed(models.Model):
    '''Model to employed personal'''

    #contador
    #administrador
    JOB_CHOICES = (
        ('0',' Contador'),
        ('1',' Administrador'),
        ('2', 'Economista'),
        ('3', 'Otro'),
    )

    first_name = models.CharField('nombre', max_length=50)
    last_name = models.CharField('apellidos', max_length=120)
    full_name = models.CharField('Nombre completos',max_length=170, blank=True)
    job = models.CharField('trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(departamento, on_delete=models.CASCADE)
    #image = models.ImageField(upload_to=None, height_field=None, width_field=None)
    habilidades = models.ManyToManyField(Habilidades)
    vida_laboral = RichTextField()

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['-first_name']

    def __str__(self):
        return str(self.id) + ' - ' + self.first_name + ' - ' + self.last_name
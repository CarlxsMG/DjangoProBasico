from django.db import models

# import to foreignkey
from applications.departamento.models import departamento

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
    job = models.CharField('trabajo', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(departamento, on_delete=models.CASCADE)
    #image = models.ImageField(upload_to=None, height_field=None, width_field=None)

    def __str__(self):
        return str(self.id) + ' - ' + self.first_name + ' - ' + self.last_name
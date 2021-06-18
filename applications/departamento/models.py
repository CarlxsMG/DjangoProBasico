from django.db import models

# Create your models here.
class departamento(models.Model):
    name = models.CharField('nombre', max_length=50)
    shortName = models.CharField('nombre corto', max_length=20)
    anulate = models.BooleanField('anulado', default=False)

    def __str__(self):
        return self.id + ' - ' + self.name + ' - ' + self.shortName
from django.db import models

# Create your models here.
class departamento(models.Model):
    name = models.CharField('nombre', max_length=50, editable=False)
    shortName = models.CharField('nombre corto', max_length=20,unique=True)
    anulate = models.BooleanField('anulado', default=False)

    class Meta:
        verbose_name = "Mi departamento"
        verbose_name_plural = "Mis departamentos"
        ordering = ['-name']
        unique_together = ('name','shortName')

    def __str__(self):
        return str(self.id) + ' - ' + self.name + ' - ' + self.shortName
from django.contrib import admin

from .models import employed, Habilidades

# Register your models here.

admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
        'image',
    )

    # funcion para darle valor a full_name
    def full_name(self, obj):
        return obj.first_name + ', ' + obj.last_name + ' - ' + str(len(obj.first_name+obj.last_name))

    search_fields = (
        'first_name',
        'last_name'
    )

    list_filter = (
        'job',
        'habilidades',
        'departamento',
    )
    #parametro solo para muchos a muchos
    filter_horizontal = ('habilidades',)

admin.site.register(employed, EmpleadoAdmin)
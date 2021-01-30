from django.contrib import admin
from .models import Empleado, Habilidades





class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name', # este campo será la concatenacion de first_name y last_name
        )

    # Creamos una funcion del nuevo campo que agregaremos visualmente
    def full_name(self, obj):
        # Toda la operacion que necesitemos
        print(obj.first_name)
        return obj.first_name + ' ' + obj.last_name
    # 

    search_fields = ('first_name',)  # creamos un filtro por campo de texto
    list_filter = ('departamento', 'job', 'habilidades',)           # creamos un filtro de seleccion
    filter_horizontal = ('habilidades',)  # filter_horizontal es util para campos relacionados de muchos a muchos, es un textarea con filter muy util



# Register your models here.
admin.site.register(Empleado, EmpleadoAdmin)
admin.site.register(Habilidades)
from django.contrib import admin
from eisula.horariosMaterias.models import Seccion, Clase

class SeccionAdmin(admin.ModelAdmin):
    list_display = ('asignatura','seccion')


class ClaseAdmin(admin.ModelAdmin):
    list_display = ('asignatura', 'seccion', 'dia', 'horaIni', 'horaFin')

admin.site.register(Seccion, SeccionAdmin)
admin.site.register(Clase, ClaseAdmin)

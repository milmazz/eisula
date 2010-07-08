from django.contrib import admin
from eisula.solicitudes.models import Estudiante, Solicitud, \
                                      Decision, DirectorEscuela, \
                                      Reglamento, Semestre

class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'cid')
    list_filter = ['cid']
    search_fields = ['cid']

class SolicitudAdmin(admin.ModelAdmin):
    list_display = ('id', 'estudiante', 'tipo', 'estado', 'fecha')
    list_filter = ['estudiante', 'tipo', 'estado']

class DecisionAdmin(admin.ModelAdmin):
    list_display = ('solicitud', 'resultado')

class DirectorEscuelaAdmin(admin.ModelAdmin):
    list_display = ('quien', 'inicio_gestion', 'fin_gestion')

class ReglamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class SemestreAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'inicio', 'fin')

admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Solicitud, SolicitudAdmin)
admin.site.register(Decision, DecisionAdmin)
admin.site.register(DirectorEscuela, DirectorEscuelaAdmin)
admin.site.register(Reglamento, ReglamentoAdmin)
admin.site.register(Semestre, SemestreAdmin)

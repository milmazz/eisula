from django.contrib import admin
from eisula.miembros.models import Miembro, Titulo, Publicacion, \
                                   GrupoInvestigacion, Departamento, \
                                   CV

class CVInline(admin.TabularInline):
    model = CV
    max_num = 1


class TituloInline(admin.TabularInline):
    model = Titulo
    max_num = 3


class MiembroAdmin(admin.ModelAdmin):
    model = Miembro
    inlines = [CVInline, TituloInline]
    search_fields = ('user', 'cedula' )


class PublicacionAdmin(admin.ModelAdmin):
    filter_horizontal = ('autores',)

class GrupoInvestigacionAdmin(admin.ModelAdmin):
    # TODO: Port telef field to Django > 1.0
    #fields = ('nombre', 'codigo', 'departamento',
    #          'responsable', 'pcontacto', 'telef', 
    #          'direccion','web', 'miembros', 'descripcion')
    fields = ('nombre', 'codigo', 'departamento',
              'responsable', 'pcontacto', 
              'direccion','web', 'miembros', 'descripcion')
    #list_display = ('codigo', 'nombre', 'responsable', 'pcontacto', 'telef')
    list_display = ('codigo', 'nombre', 'responsable', 'pcontacto')
    search_fields = ('nombre', 'codigo', 'responsable')
    list_filter = ('departamento',)
    filter_horizontal = ('miembros',)


class DepartamentoAdmin(admin.ModelAdmin):
    #fields = ('nombre', 'jefe', 'telef', 'direccion',
    #          'web', 'miembros', 'descripcion')
    fields = ('nombre', 'jefe', 'direccion',
              'web', 'miembros', 'descripcion')
    #list_display = ('nombre', 'jefe', 'telef')
    list_display = ('nombre', 'jefe')
    filter_horizontal = ('miembros',)
       

admin.site.register(Miembro, MiembroAdmin)
admin.site.register(Titulo)
admin.site.register(Publicacion, PublicacionAdmin)
admin.site.register(GrupoInvestigacion, GrupoInvestigacionAdmin)
admin.site.register(Departamento, DepartamentoAdmin)

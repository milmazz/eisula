# -*- coding: latin-1 -*-

from django.db import models

from eisula.miembros.models import Miembro

from datetime import date

from os import getcwd

#Lugar en el que se van a guardar los reglamentos
path_reglamentos = getcwd() + '/solicitudes/reglamentos/'

estado_solicitud = (
    ('N', 'No presentada'),
    ('E', 'Entregada'),
    ('T', 'Tramitada'),
    )

tipo_solicitud = (
    ('prelacion', 'Rompimiento de prelación'),
    ('exceso', 'Exceso de créditos'),
    ('colision', 'Colisión de horarios'),
    ('prorroga', 'Prorroga proyecto de grado'),
    ('regimen', 'Regimen especial'),
    ('ingresocpu', 'Ingreso de CPU a EISULA')
    )

resultado = (
    ('A', 'Aprobada'),
    ('R', 'Rechazada'),
    )

class Estudiante ( models.Model ) :
    
    nombre = models.CharField(maxlength = 32, blank = False)
    cid = models.CharField(maxlength = 16, unique = True, blank = False,
                           verbose_name = 'Cédula')

    def __str__ (self):
        return self.nombre + ". " + self.cid

    class Admin:
        list_display = ('nombre', 'cid')
        list_filter = ['cid']
        search_fields = ['cid']
    
class Solicitud ( models.Model ) :
    
    estudiante = models.ForeignKey('Estudiante', blank = False)
    tipo = models.CharField(maxlength = 16, choices = tipo_solicitud,
                            blank = False)
    estado = models.CharField(maxlength = 1, choices = estado_solicitud,
                              default = estado_solicitud[0][0])
    fecha = models.DateTimeField(auto_now = True)

    def __str__(self):
        try:
            self.id
            return str(self.id)

        except NameError:
            return self.estudiante 

    class Admin:
        list_display = ('id', 'estudiante', 'tipo', 'estado', 'fecha')
        list_filter = ['estudiante', 'tipo', 'estado']

    class Meta :
        verbose_name_plural = 'Solicitudes'

class Decision ( models.Model ) :

    solicitud = models.OneToOneField('Solicitud', blank = False)
    resultado = models.CharField(maxlength = 1, choices = resultado,
                                 blank = False)
    motivos = models.TextField(blank = False)

    class Admin:
        list_display = ('solicitud', 'resultado')

    class Meta :
        verbose_name_plural = 'Decisiones'

class DirectorEscuela ( models.Model ) :

    quien = models.ForeignKey(Miembro, blank = False, verbose_name = 'Nombre')
    inicio_gestion = models.DateField(blank = False, verbose_name =
                                      'Inicio gestión')
    fin_gestion = models.DateField(blank = False, verbose_name =
                                   'Fin gestión')

    def __str__ (self):
        return self.quien.user.get_full_name()

    class Admin :
        list_display = ('quien', 'inicio_gestion', 'fin_gestion')

    class Meta :
        verbose_name_plural = 'Directores de escuela'

class Reglamento ( models.Model ) :

    nombre = models.CharField(maxlength = 100, blank = False)
    archivo = models.FileField(upload_to = path_reglamentos)

    def __str__(self):
        return self.nombre

    class Admin :
        list_display = ('nombre',)

class Semestre ( models.Model ) :

    codigo = models.CharField(maxlength = 6, unique = True, blank = False,
                              help_text = 'Ej. A-2007')
    inicio = models.DateField(blank = False)
    fin = models.DateField(blank = False)

    def __str__ (self):
        return self.codigo

    class Admin :
        list_display = ('codigo', 'inicio', 'fin')

# -*- coding: latin-1 -*-

from datetime import date
from os import getcwd
from django.db import models
from eisula.miembros.models import Miembro

# Lugar en el que se van a guardar los reglamentos
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

class Estudiante(models.Model):  
    nombre = models.CharField(max_length=32, blank=False)
    cid = models.CharField(max_length=16, unique=True, blank=False,
                           verbose_name='Cédula')

    def __unicode__(self):
        return u"%s. %s" % (self.nombre, self.cid)
    
class Solicitud(models.Model):
    estudiante = models.ForeignKey('Estudiante', blank=False)
    tipo = models.CharField(max_length=16, choices=tipo_solicitud,
                            blank=False)
    estado = models.CharField(max_length=1, choices=estado_solicitud,
                              default=estado_solicitud[0][0])
    fecha = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        try:
            self.id
            return self.id #str(self.id)
        except NameError:
            return self.estudiante 

    class Meta:
        verbose_name_plural = 'Solicitudes'

class Decision(models.Model):
    solicitud = models.OneToOneField('Solicitud', blank=False)
    resultado = models.CharField(max_length=1, choices=resultado,
                                 blank=False)
    motivos = models.TextField(blank=False)

    class Meta :
        verbose_name_plural = 'Decisiones'

class DirectorEscuela(models.Model):
    quien = models.ForeignKey(Miembro, verbose_name = 'Nombre')
    inicio_gestion = models.DateField(verbose_name='Inicio gestión')
    fin_gestion = models.DateField(verbose_name='Fin gestión')

    def __unicode__ (self):
        return self.quien.user.get_full_name()

    class Meta :
        verbose_name_plural = 'Directores de escuela'

class Reglamento(models.Model):
    nombre = models.CharField(max_length=100)
    archivo = models.FileField(upload_to = path_reglamentos)

    def __unicode__(self):
        return self.nombre

class Semestre(models.Model):
    codigo = models.CharField(max_length=6, unique=True,
                              help_text = 'Ej. A-2007')
    inicio = models.DateField()
    fin = models.DateField()

    def __unicode__ (self):
        return self.codigo

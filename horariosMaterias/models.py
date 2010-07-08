# -*- coding: latin-1 -*-
# vim: ts=4:sts=4:tw=78:et:ai
from django.db import models
from eisula.pensum.models import Asignatura
from eisula.solicitudes.models import Semestre
from eisula.miembros.models import Miembro

DIAS_SEMANA_CHOICES =(
    ('L','Lunes'),  
    ('M','Martes'),
    ('I','Miercoles'),
    ('J','Jueves'),
    ('V','Viernes'),
    ('S','Sabado'),
    ('D','Domingo')
)


class Seccion(models.Model):
    asignatura = models.ForeignKey(Asignatura)
    semActual = models.ForeignKey(Semestre)
    seccion = models.CharField(max_length=1)
    profesor = models.ForeignKey(Miembro)
	
    def __unicode__(self):
        return self.seccion

    class Meta:
        verbose_name_plural = 'Secciones'


class Clase(models.Model):
    asignatura = models.ForeignKey(Asignatura)
    seccion = models.ForeignKey(Seccion)
    semActual = models.ForeignKey(Semestre)
    profesor = models.ForeignKey(Miembro)
    dia = models.CharField(max_length=1, choices=DIAS_SEMANA_CHOICES)
    #horaIni = models.IntegerField(verbose_name='hora inicio')
    horaIni = models.CharField(max_length=5, help_text="Formato: HH:MM",verbose_name='hora inicio')
    #horaFin = models.IntegerField(verbose_name='hora fin')
    horaFin = models.CharField(max_length=5, help_text="Formato: HH:MM",verbose_name='hora fin')

    def __unicode__(self):
        return self.dia

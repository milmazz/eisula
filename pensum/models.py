# -*- coding: latin-1 -*-

from django.db import models
from eisula.miembros.models import Departamento
from eisula.pg.models import postgrado

#Clase Materia
#Nota: Estas materias no incluyen el modelo con las horas y los profesores asignados a cada semestre

PENSUM_CHOICES = (
('P80', 'Viejo'),
('P05', 'Nuevo'),
)

SEMESTRE_CHOICES = (
    ('1','Primer Semestre'),
    ('2','Segundo Semestre'),
    ('3','Tercer Semestre'),
    ('4','Cuarto Semestre'),
    ('5','Quinto Semestre'),
    ('6','Sexto Semestre'),
    ('7','Septimo Semestre'),
    ('8','Octavo Semestre'),
    ('9','Noveno Semestre'),	
    ('10','Decimo Semestre'),
)


class Asignatura(models.Model):
	
	#Campo Texto para el nombre de la materia
	nombre = models.CharField(maxlength=500,blank=False,unique=True,verbose_name='Nombre',core=True)
	
	#La materia esta adscrita a un solo departamento
	dpto = models.ForeignKey(Departamento)
	
	#Campo texto para el codigo de la materia
	codigo = models.CharField(maxlength=25)

	#Semeste segun lo especificado SEMESTRE_CHOICES
	sem = models.CharField(maxlength=2, choices=SEMESTRE_CHOICES, default='1')

	#Si la materia pertenece al postgrado este valor tendra el id del PG
	#en caso contrario estaria ajustado a nulo
	pg = models.ForeignKey(postgrado,null=True,blank=True,default=None)

	#Unidades de Credito
	creditos = models.IntegerField(blank = False)
	
	def __str__(self):
		return self.nombre
	class Admin:
		pass

class Prelaciones(models.Model):
	#Materia que prela
	origen = models.ForeignKey(Asignatura,null=False,blank=False,verbose_name='Materia que prela',related_name='Origen')

	#Materia prelada
	destino = models.ForeignKey(Asignatura,null=False,blank=False,verbose_name='Materia Prelada',related_name='Destino')

	def __str__(self):
		return self.origen.nombre+'->'+self.destino.nombre

	class Admin:
		pass
	
	class Meta:
		verbose_name_plural= "Prelaciones"

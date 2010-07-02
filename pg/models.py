# -*- coding: latin-1 -*-

from django.db import models
from eisula.miembros.models import Departamento

#Clase Postgrado
class postgrado(models.Model):
	#Campos Texto para la ubicacion y Titulo obtenido del postgrado
	location = models.CharField(maxlength=1000,blank=True,verbose_name='Ubicacion')
	#En el caso del titulo asumimos que debe ser unico por lo
	#que se le dice a la BD que cree un indice para este
	degree = models.CharField(db_index=True,unique=True,maxlength=200,verbose_name='Titulo Obtenido')
	
	#Relacion Many2One con Departamento
	dpto = models.ForeignKey(Departamento)
	
	#El Descriptor principal del modelo es el titulo
	#asi evitamos el valor por omision (id en la BD)
	def __str__(self):
		return self.degree
	class Admin:
		pass
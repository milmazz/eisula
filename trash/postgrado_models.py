from django.db import models
import departamento

class postgrado(models.Model):
		"Clase Postgrado"
			
		#Campos Texto para la ubicacion y Titulo obtenido del postgrado
		location = TextField()
		#En el caso del titulo asumimos que debe ser unico por lo
		#que se le dice a la BD que cree un indice para este
		degree = TextField(db_index=True)
		
		#Relacion Many2One con Departamento
		dpto = models.ForeignKey(departamento)
		
		#El Descriptor principal del modelo es el titulo
		#asi evitamos el valor por omision (id en la BD)
		def __unicode__(self):
			return self.degree

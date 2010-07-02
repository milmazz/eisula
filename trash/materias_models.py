from django.db import models
import departamento
import postgrado
import persona

class subject(models.Model):
	"Clase Materias"
	
	#Campo Texto para el nombre de la materia
	name = models.TextField()
	
	#Relacion Many2One con la tabla persona
	#dado que un solo profesor imparte la materia
	#de asumir que varios profesores pueden estar asignados descomentar
	#la siguiente linea
	#tced = models.ManyToManyField(persona,related_name='prof_encargados')
	tced = models.ForeignKey(persona)
	
	#La materia esta adscrita a un solo departamento
	dpto = models.ForeignKey(departamento)
	
	#Si la materia pertenece al postgrado este valor tendra el id del PG
	#en caso contrario estaria ajustado a nulo
	pg = models.ForeignKey(postgrado,null=True)
	
	#Relacion Many2Many consigo misma, dado que una materia puede prelar y
	#ser prelada por muchas otras materias
	prelacion = models.ManyToManyField('self',related_name='mat_prelacion')
	
	def __str__(self):
		return self.name
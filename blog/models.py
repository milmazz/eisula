from django.db import models
#from django.contrib.auth.models import User
from eisula.miembros.models import Miembro

class Categoria(models.Model):
	nombre = models.CharField(max_length=32, unique=True)
	slug = models.SlugField()
	descripcion = models.TextField(blank=True)

	def __unicode__(self):
		return self.nombre
	
	def get_absolute_url(self):
		return '/noticias/categorias/%s' % (self.slug)


class Noticia(models.Model):
	titulo = models.CharField(max_length=64)
	sub_titulo = models.CharField(max_length=32, blank=True)
	slug = models.SlugField(unique_for_date='fecha_pub')
	#autor = models.ForeignKey(User)
	autor = models.ForeignKey(Miembro)
	contenido = models.TextField()
	fecha_pub = models.DateTimeField('fecha de publicacion')
	categorias = models.ManyToManyField(Categoria)
	comentarios = models.BooleanField(
			'habilitar comentarios?', 
			default=True
			)
	borrador = models.BooleanField(
			'borrador?', 
			default=False, 
			)

	def __unicode__(self):
		return self.titulo

	def get_absolute_url(self):
		return "/noticias/%s/%s" % (
				self.fecha_pub.strftime("%Y/%m/%d"), 
				self.slug
				)

	class Meta:
		ordering = ('-fecha_pub',)
		get_latest_by = 'fecha_pub'


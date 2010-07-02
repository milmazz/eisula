from django.db import models
#from django.contrib.auth.models import User
from eisula.miembros.models import Miembro

class Categoria(models.Model):
	nombre = models.CharField(maxlength=32, unique=True, core=True)
	slug = models.SlugField(prepopulate_from=('nombre',))
	descripcion = models.TextField(blank=True)

	def __str__(self):
		return self.nombre
	
	def get_absolute_url(self):
		return '/noticias/categorias/%s' % (self.slug)

	class Admin:
		pass

class Noticia(models.Model):
	titulo = models.CharField(maxlength=64)
	sub_titulo = models.CharField(maxlength=32, blank=True)
	slug = models.SlugField(
			prepopulate_from=('titulo',),
			unique_for_date='fecha_pub',
			)
	#autor = models.ForeignKey(User)
	autor = models.ForeignKey(Miembro)
	contenido = models.TextField()
	fecha_pub = models.DateTimeField('fecha de publicacion')
	categorias = models.ManyToManyField(
			Categoria, 
			filter_interface=models.HORIZONTAL
			)
	comentarios = models.BooleanField(
			'habilitar comentarios?', 
			default=True
			)
	borrador = models.BooleanField(
			'borrador?', 
			default=False, 
			)

	def __str__(self):
		return self.titulo

	def get_absolute_url(self):
		return "/noticias/%s/%s" % (
				self.fecha_pub.strftime("%Y/%m/%d"), 
				self.slug
				)

	class Admin:
		list_display = ('titulo', 'fecha_pub', 'autor', 'comentarios', 'borrador')
		search_fields = ('titulo', 'contenido')
		#Filtros

	class Meta:
		ordering = ('-fecha_pub',)
		get_latest_by = 'fecha_pub'


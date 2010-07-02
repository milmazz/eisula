from django.db import models

class Faq(models.Model):
	question = models.CharField(maxlength=200, verbose_name="Pregunta")
	answer = models.TextField(verbose_name="Respuesta")
	slug = models.SlugField(prepopulate_from=('question',))

	def get_absolute_url(self):
		return '/faq/%s' % (self.slug)

	def __str__(self):
		return self.question

	class Admin:
		pass

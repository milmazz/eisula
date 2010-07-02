from django.db import models

class Faq(models.Model):
	question = models.CharField(max_length=200, verbose_name="Pregunta")
	answer = models.TextField(verbose_name="Respuesta")

	def get_absolute_url(self):
		return '/faq/%s' % (self.slug)

	def __unicode__(self):
		return self.question

from django.conf.urls.defaults import *
from eisula.miembros.models import Publicacion

urlpatterns = patterns('django.views.generic.list_detail',
	(r'^(?P<object_id>\d+)/$', 'object_detail', {'queryset': Publicacion.objects.all()}),
	(r'^list/page(?P<page>\d+)/$', 'object_list', {'queryset': Publicacion.objects.all()}),
)


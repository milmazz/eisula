from django.conf.urls.defaults import *
from eisula.miembros.models import Departamento
from eisula.miembros.views import list_members

dpto_list_info = {
	'queryset': Departamento.objects.all(),
	'allow_empty': True,
#	'paginate_by': 10,
}

dpto_detail_info = {
	'queryset': Departamento.objects.all()
}

urlpatterns = patterns('django.views.generic.list_detail',
	(r'^list/page(?P<page>\d+)/$', 'object_list', dpto_list_info),
	(r'^(?P<object_id>\d{1,3})/$', 'object_detail', dpto_detail_info),
)

urlpatterns += patterns('',
	(r'^(?P<id>\d{1,3})/miembros/$', list_members, {'Object': Departamento}),
)


from django.conf.urls.defaults import *
from eisula.miembros.models import GrupoInvestigacion
from eisula.miembros.views import list_members

grupo_list_info = {
	'queryset': GrupoInvestigacion.objects.all(),
	'allow_empty': True,
#	'paginate_by': 10,
}

grupo_detail_info = {
	'queryset': GrupoInvestigacion.objects.all()
}

urlpatterns = patterns('django.views.generic.list_detail',
	(r'^list/page(?P<page>\d+)/$', 'object_list', grupo_list_info),
	(r'^(?P<object_id>\d{1,3})/$', 'object_detail', grupo_detail_info),
)

urlpatterns += patterns('',
	(r'^(?P<id>\d{1,3})/miembros/$', list_members, {'Object': GrupoInvestigacion}),
)


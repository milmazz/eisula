from django.conf.urls.defaults import *
from eisula.miembros.models import Miembro
from eisula.miembros.views import member_detail

members_list_info = {
	'queryset': Miembro.objects.all(),
	'allow_empty': True,
#	'paginate_by': 10,
}

urlpatterns = patterns('',
	#(r'^list/page(?P<page>\d+)/$', 'django.views.generic.list_detail.object_list', members_list_info),
	(r'^(?P<page>\d+)/$', 'django.views.generic.list_detail.object_list', members_list_info),
	(r'^(\w{1,30})/$', member_detail),
)

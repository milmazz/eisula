from django.conf.urls.defaults import *
from models import Faq

info_dict = {
		'queryset' : Faq.objects.all(),
		}

urlpatterns = patterns('',
    (r'(?P<slug>[-\w]+)/$',
	    'django.views.generic.list_detail.object_detail',
	    dict(info_dict, slug_field='slug')),
    (r'', 'django.views.generic.list_detail.object_list', info_dict),
)

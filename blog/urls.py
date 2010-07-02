from django.conf.urls.defaults import *
from models import Noticia, Categoria

news_dict = {
		'queryset' : Noticia.objects.all(),
		'date_field' : 'fecha_pub',
		}

tags_dict = {
		'queryset' : Categoria.objects.all(),
		}

urlpatterns = patterns('',
    (r'(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
	    'django.views.generic.date_based.object_detail',
	    dict(news_dict, slug_field='slug', month_format='%m')),
    (r'(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$',
    'django.views.generic.date_based.archive_day', dict(news_dict,
	    month_format='%m')),
    (r'(?P<year>\d{4})/(?P<month>\d{1,2})/$',
	    'django.views.generic.date_based.archive_month',
	    dict(news_dict, month_format='%m')),
    (r'(?P<year>\d{4})/$',
	    'django.views.generic.date_based.archive_year', news_dict),

    (r'categorias/(?P<slug>[-\w]+)/$',
	    'django.views.generic.list_detail.object_detail',
	    dict(tags_dict, slug_field='slug')),
    (r'categorias/$', 'django.views.generic.list_detail.object_list', tags_dict),
    
    (r'','django.views.generic.date_based.archive_index', news_dict ),
)

from django.conf.urls.defaults import *
from django.views.generic import date_based, list_detail
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
	    date_based.object_detail,
	    dict(news_dict, slug_field='slug', month_format='%m')),
    (r'(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$',
        date_based.archive_day, dict(news_dict, month_format='%m')),
    (r'(?P<year>\d{4})/(?P<month>\d{1,2})/$',
	    date_based.archive_month, dict(news_dict, month_format='%m')),
    (r'(?P<year>\d{4})/$',
	    date_based.archive_year, news_dict),
    (r'', date_based.archive_index, news_dict ),
)

urlpatterns += patterns('',
    (r'categorias/(?P<slug>[-\w]+)/$',
	    list_detail.object_detail,
	    dict(tags_dict, slug_field='slug')),
    (r'categorias/$', list_detail.object_list, tags_dict),
)

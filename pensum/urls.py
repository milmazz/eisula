from django.conf.urls.defaults import *
from django.conf import settings
from django.views.static import serve

urlpatterns = patterns('eisula.pensum.views',
    (r'^$', 'index'),
    (r'^(?P<asignatura_id>\d+)/$', 'single_subject'),
)
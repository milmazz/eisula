from django.conf.urls.defaults import *

urlpatterns = patterns('eisula.pg.views',
    (r'^$', 'index'),
    (r'^single_pg/$', 'single_pg'),
)
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'eisula.horariosMaterias.views.index'),
)

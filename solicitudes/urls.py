from django.conf.urls.defaults import *

urlpatterns = patterns('eisula.solicitudes.views',
    (r'^([a-z]+/|)$', 'solicitudes'),
    (r'^([a-z]+)/generar/$', 'generar_oficio'),
    (r'^generada/([a-zA-Z0-9_]+)/$', 'enviar_oficio'),
    (r'^reglamentos/(\d+)/$', 'enviar_reglamento')
)

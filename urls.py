from django.conf.urls.defaults import *
from django.conf import settings
from django.views.static import serve

urlpatterns = patterns('',
    (r'^miembros/', include('eisula.miembros.urls_miembros')),
    (r'^dpto/', include('eisula.miembros.urls_dpto')),
    (r'^grupo/', include('eisula.miembros.urls_grupo')),
    (r'^publicacion/', include('eisula.miembros.urls_publicacion')),
    (r'^noticias/', include('eisula.blog.urls')),
    (r'^pensum/', include('eisula.pensum.urls')),
    (r'^pg/', include('eisula.pg.urls')),
    (r'^faq/', include('eisula.faq.urls')),
    (r'^solicitudes/', include('eisula.solicitudes.urls')),
    (r'^horarios/', include('eisula.horariosMaterias.urls')),
    (r'^comments/', include('django.contrib.comments.urls.comments')),
    (r'^admin/', include('django.contrib.admin.urls')),
)

#Servir ficheros estaticos
#if settings.DEBUG:
#	urlpatterns +=('',
#			(r'^m/(?P<path>.*)$', server, {'document_root' :
#				'/path/absoluto/a/media'})
#			)

from django.conf.urls.defaults import *
from django.contrib import admin
from eisula import settings

admin.autodiscover()

urlpatterns = patterns('',
    #(r'^miembros/', include('eisula.miembros.urls_miembros')),
    #(r'^dpto/', include('eisula.miembros.urls_dpto')),
    #(r'^grupo/', include('eisula.miembros.urls_grupo')),
    #(r'^publicacion/', include('eisula.miembros.urls_publicacion')),
    #(r'^noticias/', include('eisula.blog.urls')),
    #(r'^pensum/', include('eisula.pensum.urls')),
    #(r'^pg/', include('eisula.pg.urls')),
    (r'^faq/', include('eisula.faq.urls')),
    #(r'^solicitudes/', include('eisula.solicitudes.urls')),
    #(r'^horarios/', include('eisula.horariosMaterias.urls')),
    #(r'^comments/', include('django.contrib.comments.urls.comments')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)

#Servir ficheros estaticos
if settings.DEBUG:
	urlpatterns += patterns('',
			(r'^m/(?P<path>.*)$', 'django.views.static.serve', {'document_root' :
				settings.STATIC_DOC_ROOT})
			)

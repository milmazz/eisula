from django.contrib import admin
from eisula.blog.models import Categoria, Noticia

class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug' : ('nombre',)
    }

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_pub', 'autor', 'comentarios', 'borrador')
    search_fields = ('titulo', 'contenido')
    prepopulated_fields = {
        'slug': ('titulo',)
    }
    filter_horizontal = ('categorias',)

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Noticia, NoticiaAdmin)


# vim: et:ai:sts=4:ts=4:nowrap
from django.views.generic.list_detail import object_list
from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from eisula.miembros.models import *

def member_detail(request, username_):
	member = get_object_or_404(Miembro, user__username=username_)
	buffer= {}
    buffer['username'] = member.user.username
	buffer['first_name'] = member.user.first_name
	buffer['last_name'] = member.user.last_name
	buffer['email'] = member.user.email
    buffer['sexo'] = member.sexo
    buffer['web'] = member.web
    try:
        cv = member.cv_set.all()[0]
        buffer['nacionalidad'] = cv.nacionalidad
        buffer['categoria'] = cv.categoria
        buffer['publicaciones'] = cv.publicacion_set.all()
    except:
        pass
    try:
        buffer['departamento'] = member.departamento_set.all()[0]
    # TODO, manejar la exception. Escribir logs??
    except:
        pass

    buffer['titulos'] = member.titulo_set.all()
    buffer['grupos'] = member.grupoinvestigacion_set.all()

	return render_to_response('miembros/miembro_detail.html', buffer)


def list_members(request, Object, id):
    try:
        members = Object.objects.get(pk=id).miembros.all()
    # TODO, majenar except!
    except:
        raise Http404

    return object_list(request, queryset=members)

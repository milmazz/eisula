from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, loader
from django.template import Template, Context

from os import getcwd, system
from os.path import join

from string import capwords, split

from eisula.solicitudes.models import *
from eisula.solicitudes.utils import *

from eisula.pensum.models import Asignatura
from eisula.miembros.models import Miembro, Departamento

#Lugar en el que se van a generar los archivos de solicitud
tex_pdf_dir = join(getcwd(), 'solicitudes', 'tex_pdf')
#Lugar en el que se van a guardar los formatos de solicitud en latex
reglamentos_dir = join(getcwd(), 'solicitudes', 'reglamentos')

def solicitudes (request, form) :

    f = "prelacion/"
    if form:
        f = form

    semestres = Semestre.objects.all()
    materias = Asignatura.objects.all()
    reglamentos = Reglamento.objects.all()
    departamentos = Departamento.objects.all()

    miembros = []

    for m in Miembro.objects.all():
        miembros.append(m.user.get_full_name())
    
    return render_to_response ('solicitudes/solicitudes.html', locals())

def guardar_estudiante (nom, ced) :
    
    try:
        e = Estudiante.objects.get(cid = ced)
        
    except Estudiante.DoesNotExist:
        e = Estudiante(nombre = nom, cid = ced)
        e.save()

    return e

#Genera el oficio de solicitud segun el formato requerido
def generar_oficio (request, formato) :

    post = request.POST

    datos = {'prelacion' : datos_prelacion,
             'exceso' : datos_exceso,
             'colision' : datos_colision,
             'prorroga' : datos_prorroga,
             'regimen' : datos_regimen,
             'ingresocpu' : datos_ingresocpu,
             }

    nombre_estudiante = post['nombre']
    cid_estudiante = post['nac'] + '-' + post['cedula']

    e = guardar_estudiante(nombre_estudiante, cid_estudiante)

    s = Solicitud(estudiante = e, tipo = formato)
    s.save()

    #Nombre de plantilla en latex para formato
    tex_tpl_filename = 'solicitudes/formatos/' + formato + '.tex'

    #Nombre de archivos a generar
    filename = "EISULA_%s_%d" % (s.tipo, s.id);
    
    tex_filename = join (tex_pdf_dir, filename + '.tex')
    pdf_filename = join (tex_pdf_dir, filename + '.pdf')
    
    variables = datos[formato](post)
    variables['regimen'] = formato == 'regimen'
    variables['id'] = s.id

    #t tiene el contenido del oficio de solicitud como cadena
    t = loader.render_to_string(tex_tpl_filename, variables)

    open (tex_filename, 'w').write(t)

    system ('pdflatex -output-directory ' + tex_pdf_dir + ' '
            + tex_filename)
    
    return HttpResponseRedirect ('/solicitudes/generada/' + filename + '/')

#Envia respuesta con el oficio de solicitud generado en formato pdf
def enviar_oficio (request, filename) :

    contenido = 'attachment; filename = %s.pdf' % filename
    response = HttpResponse (mimetype = 'application/pdf')
    response['Content-Disposition'] = contenido

    response.write (open(join(tex_pdf_dir, filename + '.pdf'), 'r').read())

    system('rm ' + join(tex_pdf_dir, filename) + '*')
    
    return response

def enviar_reglamento (request, reglamento) :

    r = Reglamento.objects.get(id = reglamento)

    filename = split(r.archivo, "/")[-1]

    contenido = 'attachment; filename = ' + filename
    response = HttpResponse (mimetype = 'application/pdf')
    response['Content-Disposition'] = contenido

    response.write (open(r.archivo, 'r').read())

    return response

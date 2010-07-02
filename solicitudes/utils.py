from eisula.solicitudes.models import DirectorEscuela

from eisula.pensum.models import Asignatura
from eisula.miembros.models import Departamento, Miembro

from string import lower, capitalize

from datetime import date

#Devuelve el director actual de la escuela
def director_actual ():
    
    directores = DirectorEscuela.objects.all()

    for d in directores:
        if d.inicio_gestion <= date.today() and date.today() <= d.fin_gestion:
            return d

    return None

#La letras que difiere entre dirigir a profesor y a profesora
#consejo debe ser 'escuela' o el nombre de algun departamento
def letras_titulo (consejo):

    if consejo == 'escuela':
        d = director_actual()
        
        if d.quien.sexo == 'F':
            return 'a'

        return ''

    else:
        d = Departamento.objects.get(nombre = consejo).jefe

        if d.sexo == 'F':
            return 'a', 'a'

        return '', 'e'
        
def hacer_motivos (post) :

    post_keys = post.keys()[0:];
    motivos = []
    post_keys.sort()

    #Chequeos para que los motivos de solicitud queden bien
    #en el oficio
    for k in post_keys:
        if k[0:-1] == 'motivo':
            m = capitalize(post[k][0:])

            if(m[-1] == '.'):
                m = m[0:-1]
            
            motivos.append(m)
            
    numero_motivos = len(motivos)
    
    if numero_motivos == 1:
        motivos[0] = lower(motivos[0][0]) + motivos[0][1:]

    return motivos, numero_motivos

def hacer_materias (post) :

    post_keys = post.keys()[0:];
    materias = []
    post_keys.sort()

    #Chequeos para que los motivos de solicitud queden bien
    #en el oficio
    for k in post_keys:
        if k[0:-1] == 'materia':
            m = Asignatura.objects.get(nombre = post[k])
            
            materias.append(m)
            
    return materias

def datos_comunes (post) :

    hm = hacer_motivos(post)

    datos = {'nombre_estudiante' : post['nombre'],
             'cedula_estudiante' : post['nac'] + '-' + post['cedula'],
             'motivos' : hm[0],
             'numero_motivos' : hm[1]
            }
    
    return datos

def datos_prelacion (post):

    datos = datos_comunes(post)

    d = director_actual()
    
    datos['nombre_director'] = d.quien.user.get_full_name()
    datos['letra'] = letras_titulo('escuela')
    datos['materia1'] = post['materia1']
    datos['materia2'] = post['materia2']
    datos['semestre'] = post['semestre']
    
    return datos

def datos_exceso (post):

    datos = datos_comunes(post)

    d = director_actual()

    datos['nombre_director'] = d.quien.user.get_full_name()
    datos['letra'] = letras_titulo('escuela')
    datos['materias'] = hacer_materias(post)
    datos['exceso'] = post['exceso']
    datos['semestre'] = post['semestre']

    total = 0
    for m in datos['materias']:
        total += m.creditos

    datos['total'] = total

    return datos

def datos_colision (post):

    datos = datos_comunes(post)

    d = director_actual()

    datos['nombre_director'] = d.quien.user.get_full_name()
    datos['letra'] = letras_titulo('escuela')
    datos['horas'] = post['horas']
    datos['materia1'] = post['materia1']
    datos['materia2'] = post['materia2']
    datos['semestre'] = post['semestre']

    return datos

def datos_prorroga (post):

    datos = datos_comunes(post)

    d = Departamento.objects.get(nombre = post['departamento'])
    letras = letras_titulo(post['departamento'])

    datos['nombre_jefe'] = d.jefe.user.get_full_name()
    datos['letra_prof'] = letras[0]
    datos['letra_jefe'] = letras[1]
    datos['nombre_jefe'] = d.jefe.user.get_full_name()
    datos['departamento'] = d.nombre
    datos['titulo_proyecto'] = post['titulo']
    datos['semestre'] = post['semestre']
    datos['dep_tutor'] = post['dep_tutor']
    datos['nombre_tutor'] = post['tutor']
    datos['porcentaje'] = post['porcentaje']
    datos['dia'] = post['dia']
    datos['mes'] = post['mes']
    datos['year'] = post['year']

    return datos

def datos_regimen (post):

    datos = datos_comunes(post)

    d = Departamento.objects.get(nombre = post['departamento'])
    letras = letras_titulo(post['departamento'])

    datos['nombre_jefe'] = d.jefe.user.get_full_name()
    datos['letra_prof'] = letras[0]
    datos['letra_jefe'] = letras[1]
    datos['nombre_jefe'] = d.jefe.user.get_full_name()
    datos['departamento'] = d.nombre
    datos['materia'] = post['materia']
    datos['profesor'] = post['profesor']

    for m in Miembro.objects.all():
        if m.user.get_full_name() == datos['profesor']:
            if m.sexo == 'F':
                datos['titulo'] = 'La Profesora'
            else:
                datos['titulo'] = 'El Profesor'
            break
            
    return datos
    
def datos_ingresocpu (post):

    datos = datos_comunes(post)

    datos['serial'] = post['serial']
    datos['otras'] = post['otras']
    datos['dia'] = post['dia']
    datos['mes'] = post['mes']
    datos['year'] = post['year']

    return datos
    

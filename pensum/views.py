# -*- coding: latin-1 -*-

from django.shortcuts import get_object_or_404, render_to_response
from eisula.pensum.models import *

#Funcion para ajustar el arreglo con las materias segun se desee (pregrado o postgrado)
#boolpg. Booleano para dictaminar si se quieren de pregrado o postgrado
def filtrar_asignaturas(lista,boolpg=False):
		fetch_asignaturas = []
		for asign in lista:
			if boolpg==False and asign.pg == None:
				fetch_asignaturas.append(asign)
			elif boolpg==True and asign.pg != None:
				fetch_asignaturas.append(asign)
		return fetch_asignaturas
	
def index(request):
	#Variable para marcar o no si se quiere el pensum de postgrado
	get_pg=False
	try:
		print request.POST['pg']
		#Se realizan estas consultas si se quieren son las materias de postgrado
		if request.POST['pg'] == 'check':
			get_pg=True
	except(KeyError):
		get_pg=False
	#Chequea que la variable POST este ajustada
	try:
		if get_pg==True:
			#Dado que se desean las materias de postgrado, esto debería mantenerse
			#Los posibles filtros de busqueda (semestre, departamento y todo)
			#la variable fetch_asignaturas se ajusta dependiendo del filtro requerido
			if request.POST['filtro'] == "semestre":
				fetch_asignaturas = filtrar_asignaturas(Asignatura.objects.filter(sem=request.POST['filter_opt']),True)
			elif request.POST['filtro'] == "departamento":
				fetch_asignaturas = filtrar_asignaturas(Asignatura.objects.filter(dpto=request.POST['filter_opt']),True)
			elif request.POST['filtro'] == "all":
				fetch_asignaturas = filtrar_asignaturas(Asignatura.objects.all().order_by('sem'),True)
		#Se realizan estas consultas si se quieren las materisa de pregrado
		else:
			#Los posibles filtros de busqueda (semestre, departamento y todo)
			#la variable fetch_asignaturas se ajusta dependiendo del filtro requerido
			if request.POST['filtro'] == "semestre":
				fetch_asignaturas = filtrar_asignaturas(Asignatura.objects.filter(sem=request.POST['filter_opt']))
			elif request.POST['filtro'] == "departamento":
				fetch_asignaturas = filtrar_asignaturas(Asignatura.objects.filter(dpto=request.POST['filter_opt']))
			elif request.POST['filtro'] == "all":
				fetch_asignaturas = filtrar_asignaturas(Asignatura.objects.all().order_by('sem'))
	#Si el POST no esta ajustado significa que se esta llamando a la pagina por primera vez
	#y no existen filtros
	except(KeyError):
		fetch_asignaturas = filtrar_asignaturas(Asignatura.objects.order_by('sem'))
	#		fetch_asignaturas = Asignatura.objects.all()
	#Obtenemos los nombres de los departamentos
	fetch_dpto = Departamento.objects.all()
	#Se renderiza el controlador para ver el pensum
	return render_to_response('pensum/index.html',{'fetch_asignaturas':fetch_asignaturas,'fetch_dpto':fetch_dpto,'get_pg':get_pg})
	
def single_subject(request,asignatura_id):
	materia = get_object_or_404(Asignatura, pk=asignatura_id)
	mat_dpto = Departamento.objects.get(pk=materia.dpto.id)
	fetch_prel = Prelaciones.objects.filter(destino=asignatura_id)
	return render_to_response('pensum/subject.html',{'materia':materia,'mat_dpto':mat_dpto,'fetch_prel':fetch_prel})

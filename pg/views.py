# -*- coding: latin-1 -*-

from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from eisula.pensum.models import postgrado

def index(request):
	fetch_pg = postgrado.objects.all().order_by('degree')
	return render_to_response('pg/index.html',{'fetch_pg':fetch_pg})

def single_pg(request):
	#Chequea que la variable POST este ajustada
	try:
		#Consigue los atributos del Postgrado
		pg=postgrado.objects.get(id=request.POST['pg_id'])
	except(KeyError):
		return HttpResponseRedirect('/pg/')
	return render_to_response('pg/single_pg.html',{'pg':pg})
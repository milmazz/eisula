from django.shortcuts import render_to_response
from eisula.horariosMaterias.models import Seccion, Clase
from eisula.miembros.models import Miembro
from eisula.pensum.models import Asignatura

def index(request):
    #latest_asignatura_list = Asignatura.objects.all().order_by('-codigo')[:5]
    clases_list = Clase.objects.all()
    return render_to_response('horariosMaterias/index.html', {'clases_list': clases_list})

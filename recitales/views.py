from django.shortcuts import render
from .models import Recital, Participacion

def recitales(request):
    recitales = Recital.objects.all()
    return render(request, 'recitales/recitales.html', {'recitales': recitales})
def recital(request, recital_id):
    participaciones = Participacion.objects.filter(recital__id=recital_id)
    recital = Recital.objects.get(id=recital_id)
    return render (request, 'recitales/recital.html', {'participaciones': participaciones, 'recital': recital})
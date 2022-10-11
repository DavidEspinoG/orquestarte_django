from django.shortcuts import render
from .models import Recital
# Create your views here.
def recitales(request):
    recitales = Recital.objects.all()
    return render(request, 'recitales/recitales.html', {'recitales': recitales})
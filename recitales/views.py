from django.shortcuts import render

# Create your views here.
def recitales(request):
    return render(request, 'recitales/recitales.html')
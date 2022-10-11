from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')
def virtuales(request):
    return render(request, 'core/virtuales.html')
def presenciales(request):
    return render(request, 'core/presenciales.html')
def recitales(request):
    return render(request, 'core/recitales.html')
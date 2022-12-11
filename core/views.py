from django.shortcuts import render, redirect
from django.contrib.auth import logout

def home(request):
    return render(request, 'core/home.html')

def virtuales(request):
    return render(request, 'core/virtuales.html')

def presenciales(request):
    return render(request, 'core/presenciales.html')

def logout_view(request):
    logout(request)
    return redirect('/')
from django.shortcuts import render
from django.views.generic import ListView
from .models import ClaseVirtual

class Virtuales(ListView):
    template_name = 'virtuales/virtuales.html'
    model = ClaseVirtual

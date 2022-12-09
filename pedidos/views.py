from django.shortcuts import render
from django.views.generic import TemplateView 
from .models import Pedido

def pedido(request):
    elements = Pedido.objects.all()
    total = 0
    for e in elements: 
        total += e.price
    context = {'pedido': elements, 'total': str(total)}
    return render(request, 'pedidos/carrito.html', context)
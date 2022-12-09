from django.shortcuts import render
from django.views.generic import ListView
from .models import ClaseVirtual
from pedidos.models import Pedido


def virtuales(request):
    model = ClaseVirtual.objects.all()
    context = {'object_list': model}
    return render(request, 'virtuales/virtuales.html', context)

def guardaPedido(request, **kwargs):
    model = ClaseVirtual.objects.all()
    context = {'object_list': model}
    title = kwargs.get('title')
    price = kwargs.get('price')
    pedido = Pedido(title=title, price=price)
    pedido.save()
    return render(request, 'virtuales/virtuales.html', context)
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import ClaseVirtual
from pedidos.models import Pedido

def virtuales(request):
    model = ClaseVirtual.objects.all()
    carrito = Pedido.objects.all()
    context = {'object_list': model, 'carrito': carrito}
    prueba = Pedido.objects.filter(title='Canto')
    if len(prueba) > 0:
        print(True)
    return render(request, 'virtuales/virtuales.html', context)

def guardaPedido(request, **kwargs):
    title = kwargs.get('title')
    price = kwargs.get('price')
    exist = Pedido.objects.filter(title=title)
    if len(exist) < 1:
        pedido = Pedido(title=title, price=price)
        pedido.save()
    else: 
        exist.delete()   
    return redirect('/virtuales')


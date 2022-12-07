from django.shortcuts import render
from django.views.generic import TemplateView 

class Pedido(TemplateView):
    template_name = 'pedidos/carrito.html'
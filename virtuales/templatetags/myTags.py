from django import template
from pedidos.models import Pedido
register = template.Library()

def isOnCart(value):
    query = Pedido.objects.filter(title=value)
    if len(query) > 0:
        return True
    else:
        return False

register.filter('isOnCart', isOnCart)
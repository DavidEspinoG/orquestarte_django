"""orquestarte URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views as core_views
from recitales import views as recitales_views
from pedidos import views as pedidos_views
from virtuales import views as virtuales_views
from . import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.home, name="home"),
    path('virtuales', virtuales_views.Virtuales.as_view(), name="virtuales"),
    path('presenciales', core_views.presenciales, name="presenciales"),
    path('recitales', recitales_views.recitales, name="recitales"),
    path('recital/<int:recital_id>', recitales_views.recital, name="recital"),
    path('carrito', pedidos_views.Pedido.as_view(), name="carrito"),
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, 
            document_root=settings.MEDIA_ROOT)

"""
URL configuration for luckfoody project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from PaginaWeb.views import portalpago,ingresarplatillo,carritocompra,verplatillo,pagofracaso,pagoexitoso,ingresarcatalogo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('portal_pago/',portalpago),
    path('ingresar_platillo/',ingresarplatillo),
    path('carrito_de_compra/',carritocompra),
    path('pago fracaso/',pagofracaso),
    path('pago exitoso/',pagoexitoso),
    path('ingresar catalogo/',ingresarcatalogo),
    path('ver_platillo/',verplatillo)
]

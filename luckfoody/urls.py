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
<<<<<<< HEAD
from PaginaWeb.views import portalpago,ingresarplatillo,verplatillo,pagofracaso,pagoexitoso,ingresarcatalogo,ingresarsucursal,ingresartrivia,Trivia
=======
from PaginaWeb.views import portalpago,ingresarplatillo,carritocompra,verplatillo,pagofracaso,pagoexitoso,ingresarcatalogo,Login, CrearCuenta,Administrador,Repartidor, CrearCuentaAdmin
>>>>>>> d19271b79bda43467a4d1611afd430d94c2c8851

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', Login),
    path('crear-cuenta', CrearCuenta),
    path('pagina-admin', Administrador),
    path('crear-cuenta-admin', CrearCuentaAdmin),
    path('pagina-repartidor', Repartidor),
    path('portal_pago/',portalpago),
    path('ingresar_platillo/',ingresarplatillo),
    path('carrito_de_compra/',carritocompra),
    path('pago fracaso/',pagofracaso),
    path('pago exitoso/',pagoexitoso),
    path('ingresar catalogo/',ingresarcatalogo),
    path('ingresar sucursal/',ingresarsucursal),
    path('ingresar trivia/',ingresartrivia),
    path('trivia/',Trivia),
    path('ver_platillo/',verplatillo),
    path('pagina_principal/',paginaprincipal)
]

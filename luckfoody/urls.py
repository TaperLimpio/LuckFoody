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

from PaginaWeb.views import portalpago,ingresarplatillo,carritocompra
from PaginaWeb.views import verplatillo,pagofracaso,pagoexitoso
from PaginaWeb.views import ingresarcatalogo,login, crearcuenta, paginaprincipal
from PaginaWeb.views import Administrador,Repartidor, crearcuentaadmin
from PaginaWeb.views import ingresartrivia,ver_usuario,Trivia, Update_Usuario,delete_usuario,Index_Usuario

from Sucursal_app.views import ingresarsucursal, consultarsucursal, modificarsucursal,deshabilitarsucursal
from Sucursal_app.views import deshabilitarsucursal, listasucursal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('crear-cuenta/', crearcuenta,name='crear_cuenta'),
    path('pagina-admin/', Administrador,name='administrador'),
    path('crear-cuenta-admin/', crearcuentaadmin,name='crear_cuenta_admin'),
    path('pagina-repartidor/', Repartidor,name='repartidor'),
    path('portal_pago/',portalpago),
    path('ingresar_platillo/',ingresarplatillo),
    path('carrito_de_compra/',carritocompra),
    path('pago fracaso/',pagofracaso),
    path('pago exitoso/',pagoexitoso),
    path('ingresar catalogo/',ingresarcatalogo),
    path('ingresar trivia/',ingresartrivia),
    path('trivia/',Trivia),
    path('ver_platillo/',verplatillo),
    path('usuarios/<int:emp_id>/',ver_usuario, name='ver_usuario'),
    path('pagina_principal/',paginaprincipal,name='usuario'),
    path('delete-usuario/<int:emp_id>/',delete_usuario, name='delete_usuario'),
    path('update_usuario/<int:emp_id>/', Update_Usuario),
    path('ingresar_sucursal/',ingresarsucursal),
    path('consultar_sucursal/<int:id>',consultarsucursal),
    path('modificar_sucursal/<int:id>',modificarsucursal),
    path('deshabilitar_sucursal/<int:id>',deshabilitarsucursal),
    path('index usuario/',Index_Usuario, name='index_usuario'),
    path('lista_sucursales/',listasucursal)
]

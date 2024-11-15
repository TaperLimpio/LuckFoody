from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from Catalogo_app.views import paginaprincipal, ingresarcatalogo, asignar_platillo, ver_catalogo,paginaadmin  # Importa la vista correcta desde Catalogo_app
from Catalogo_app.views import  activar_catalogo,desactivar_catalogo,ver_catalogoadmin,actualizarcatalogo

from PaginaWeb.views import portalpago, carritocompra, verplatillo, pagofracaso
from PaginaWeb.views import pagoexitoso, Repartidor, ingresartrivia, Trivia

from Pedido_app.views import consultar_pedidos, ver_pedido, mis_pedidos, cancelar_pedido

from Usuario_app.views import crearcuenta, login, crearcuentaadmin, ver_usuario 
from Usuario_app.views import Update_Usuario, delete_usuario, Index_Usuario

from Sucursal_app.views import ingresarsucursal, consultarsucursal, modificarsucursal
from Sucursal_app.views import deshabilitarsucursal, listasucursal

from Platillo_app.views import ingresarplatillo, activar_platillo 
from Platillo_app.views import desactivar_platillo, actualizarplatillo

urlpatterns = [

    #Inicio Sesión
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('crear-cuenta/', crearcuenta, name='crear_cuenta'),
    path('crear-cuenta-admin/', crearcuentaadmin, name='crear_cuenta_admin'),

    #Platillo
    path('ingresar_platillo/', ingresarplatillo, name='ingresar_platillo'),
    path('ver_platillo/', verplatillo),
    path('asignar_platillo/<int:catalogo_id>/', asignar_platillo, name='asignar_platillo'),
    path('actualizar_platillo/<int:platillo_id>/', actualizarplatillo, name='actualizar_platillo'),
    path('activar_platillo/<int:platillo_id>/', activar_platillo, name='activar_platillo'),
    path('desactivar_platillo/<int:platillo_id>/', desactivar_platillo, name='desactivar_platillo'),
    
    #Catálogo
    path('ingresar_catalogo/', ingresarcatalogo, name='ingresar_catalogo'),
    path('ver_catalogo_admin/<int:catalogo_id>/', ver_catalogoadmin, name='ver_catalogo_admin'),
    path('ver_catalogo/<int:catalogo_id>/', ver_catalogo, name='ver_catalogo'),
    path('actualizar_catalogo/<int:catalogo_id>/', actualizarcatalogo, name='actualizar_catalogo'),
    path('activar_catalogo/<int:catalogo_id>/',activar_catalogo, name='activar_catalogo'),
    path('desactivar_catalogo/<int:catalogo_id>/',desactivar_catalogo, name='desactivar_catalogo'),

    #Sucursal
    path('ingresar_sucursal/', ingresarsucursal),
    path('lista_sucursales/', listasucursal),
    path('consultar_sucursal/<int:id>/', consultarsucursal),
    path('modificar_sucursal/<int:id>/', modificarsucursal),
    path('deshabilitar_sucursal/<int:id>/', deshabilitarsucursal),

    #Páginas
    path('pagina-repartidor/', Repartidor, name='repartidor'),
    path('pagina-admin/', paginaadmin, name='pagina_administrador'),
    path('pagina_principal/', paginaprincipal, name='pagina_principal'),

    #Pedidos
    path('pedidos/', consultar_pedidos, name='pedidos'),
    path('ver_pedido/<int:pedido_id>/', ver_pedido),
    path('mis_pedidos/', mis_pedidos, name='mis_pedidos'),
    path('cancelar_pedido/<int:id_pedido>', cancelar_pedido, name='cancelar_pedido'),
    
    #Trivia
    path('ingresar trivia/', ingresartrivia),
    path('trivia/', Trivia),

    #Pagos
    path('portal_pago/', portalpago),
    path('carrito_de_compra/', carritocompra),
    path('pago fracaso/', pagofracaso),
    path('pago exitoso/', pagoexitoso),

    #Usuario
    path('index usuario/', Index_Usuario, name='index_usuario'),
    path('usuarios/<int:emp_id>/', ver_usuario, name='ver_usuario'), 
    path('delete-usuario/<int:emp_id>/', delete_usuario, name='delete_usuario'),
    path('update_usuario/<int:emp_id>/', Update_Usuario),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

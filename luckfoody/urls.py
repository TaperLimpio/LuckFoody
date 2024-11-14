from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from Catalogo_app.views import paginaprincipal, ingresarcatalogo, asignar_platillo, ver_catalogo,paginaadmin,activar_catalogo,desactivar_catalogo,ver_catalogoadmin,actualizarcatalogo  # Importa la vista correcta desde Catalogo_app

from PaginaWeb.views import portalpago, carritocompra, verplatillo, pagofracaso, pagoexitoso, Repartidor, ingresartrivia, Trivia

from Pedido_app import views

from Usuario_app.views import crearcuenta, login, crearcuentaadmin, ver_usuario, Update_Usuario, delete_usuario, Index_Usuario

from Sucursal_app.views import ingresarsucursal, consultarsucursal, modificarsucursal, deshabilitarsucursal, listasucursal

from Platillo_app.views import ingresarplatillo,activar_platillo,desactivar_platillo,actualizarplatillo  # Importa la vista para ingresar platillos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('activar_platillo/<int:platillo_id>/',activar_platillo, name='activar_platillo'),
    path('desactivar_platillo/<int:platillo_id>/',desactivar_platillo, name='desactivar_platillo'),
    path('actualizar_platillo/<int:platillo_id>/',actualizarplatillo, name='actualizar_platillo'),
    path('crear-cuenta/', crearcuenta, name='crear_cuenta'),
    path('pagina-admin/', paginaadmin, name='pagina_administrador'),
    path('actualizar_catalogo/<int:catalogo_id>/', actualizarcatalogo, name='actualizar_catalogo'),
    path('activar_catalogo/<int:catalogo_id>/',activar_catalogo, name='activar_catalogo'),
    path('desactivar_catalogo/<int:catalogo_id>/',desactivar_catalogo, name='desactivar_catalogo'),
    path('crear-cuenta-admin/', crearcuentaadmin, name='crear_cuenta_admin'),
    path('pagina-repartidor/', Repartidor, name='repartidor'),
    path('portal_pago/', portalpago),
    path('ingresar_platillo/', ingresarplatillo, name='ingresar_platillo'),
    path('carrito_de_compra/', carritocompra),
    path('pago fracaso/', pagofracaso),
    path('pago exitoso/', pagoexitoso),
    path('ingresar_catalogo/', ingresarcatalogo, name='ingresar_catalogo'),
    path('ingresar trivia/', ingresartrivia),
    path('pedidos/',views.consultar_pedidos, name='pedidos'),
    path('ver_pedido/<int:pedido_id>/', views.ver_pedido),
    path('mis_pedidos/', views.mis_pedidos, name='mis_pedidos'),
    path('cancelar_pedido/<int:id_pedido>', views.cancelar_pedido, name='cancelar_pedido'),
    path('trivia/', Trivia),
    path('ver_platillo/', verplatillo),
    path('usuarios/<int:emp_id>/', ver_usuario, name='ver_usuario'),
    path('pagina_principal/', paginaprincipal, name='pagina_principal'),  # Asegúrate de redirigir a la URL correcta
    path('delete-usuario/<int:emp_id>/', delete_usuario, name='delete_usuario'),
    path('update_usuario/<int:emp_id>/', Update_Usuario),
    path('ingresar_sucursal/', ingresarsucursal),
    path('consultar_sucursal/<int:id>/', consultarsucursal),
    path('modificar_sucursal/<int:id>/', modificarsucursal),
    path('deshabilitar_sucursal/<int:id>/', deshabilitarsucursal),
    path('index usuario/', Index_Usuario, name='index_usuario'),
    path('lista_sucursales/', listasucursal),
    path('asignar_platillo/<int:catalogo_id>/', asignar_platillo, name='asignar_platillo'),
    path('ver_catalogo/<int:catalogo_id>/', ver_catalogo, name='ver_catalogo'),  # Agrega esta línea
    path('ver_catalogo_admin/<int:catalogo_id>/', ver_catalogoadmin, name='ver_catalogo_admin'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

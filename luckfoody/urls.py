from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from Catalogo_app.views import paginaprincipal, ingresarcatalogo, asignar_platillo, ver_catalogo  # Importa la vista correcta desde Catalogo_app
from PaginaWeb.views import portalpago, carritocompra, verplatillo, pagofracaso, pagoexitoso, Administrador, Repartidor, ingresartrivia, Trivia
from Usuario_app.views import crearcuenta, login, crearcuentaadmin, ver_usuario, Update_Usuario, delete_usuario, Index_Usuario
from Sucursal_app.views import ingresarsucursal, consultarsucursal, modificarsucursal, deshabilitarsucursal, listasucursal
from Platillo_app.views import ingresarplatillo  # Importa la vista para ingresar platillos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('crear-cuenta/', crearcuenta, name='crear_cuenta'),
    path('pagina-admin/', Administrador, name='administrador'),
    path('crear-cuenta-admin/', crearcuentaadmin, name='crear_cuenta_admin'),
    path('pagina-repartidor/', Repartidor, name='repartidor'),
    path('portal_pago/', portalpago),
    path('ingresar_platillo/', ingresarplatillo, name='ingresar_platillo'),
    path('carrito_de_compra/', carritocompra),
    path('pago fracaso/', pagofracaso),
    path('pago exitoso/', pagoexitoso),
    path('ingresar_catalogo/', ingresarcatalogo, name='ingresar_catalogo'),
    path('ingresar trivia/', ingresartrivia),
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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

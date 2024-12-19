#importaciones para el funcionamiento
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

# urls de las distintas apps
from Catalogo_app.views import paginaprincipal, ingresarcatalogo, ver_catalogoadmin  
from Catalogo_app.views import  activar_catalogo,desactivar_catalogo,paginaadmin
from Catalogo_app.views import asignar_platillo, ver_catalogo,actualizarcatalogo
from Catalogo_app.views import paginarepartidor

from PaginaWeb.views import dashboard

from Pedido_app.views import consultar_pedidos, ver_pedido, mis_pedidos, cancelar_pedido

from Usuario_app.views import crearcuenta, login, crearcuentaadmin
from Usuario_app.views import Update_Usuario, desactivar_usuario, Index_Usuario
from Usuario_app.views import ver_usuario, mi_cuenta, activar_usuario
from Usuario_app.views import Update_mi_cuenta,actualizar_contraseña

from Sucursal_app.views import ingresarsucursal, consultarsucursal, modificarsucursal
from Sucursal_app.views import deshabilitarsucursal, listasucursal, habilitarsucursal

from Platillo_app.views import ingresarplatillo, activar_platillo
from Platillo_app.views import desactivar_platillo, actualizarplatillo

from Pedido_app.views import consultar_pedidos,ver_pedido,mis_pedidos
from Pedido_app.views import cancelar_pedido

from TomarPedido_app.views import aceptar_pedido,entregar_pedido

from Carrito_app.views import ver_carrito, agregar_a_carrito, aumentar_cantidad
from Carrito_app.views import disminuir_cantidad,realizar_pedido,pagoexitoso
from Carrito_app.views import pagofracaso

from Trivia_app.views import Trivias,Crear_trivia,Editar_Trivia,Preguntas
from Trivia_app.views import Crear_Preguntas,Editar_Pregunta,Respuestas
from Trivia_app.views import Crear_Respuesta,Editar_Respuesta,EstablecerCorrecta
from Trivia_app.views import Activar_Trivia,Desactiva_Trivia,Mis_trivias
from Trivia_app.views import Responder_Trivia

urlpatterns = [

    #Inicio Sesión
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('crear-cuenta/', crearcuenta, name='crear_cuenta'),
    path('crear-cuenta-admin/', crearcuentaadmin, name='crear_cuenta_admin'),

    #Platillo
    path('ingresar_platillo/', ingresarplatillo, name='ingresar_platillo'),
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
    path('lista_sucursales/', listasucursal, name='lista sucursales'),
    path('consultar_sucursal/<int:id>/', consultarsucursal),
    path('modificar_sucursal/<int:id>/', modificarsucursal),
    path('deshabilitar_sucursal/<int:id>/', deshabilitarsucursal,name="deshabilitar_sucursal"),
    path('habilitar_sucursal/<int:id>/',habilitarsucursal,name="habilitar_sucursal"),

    #Páginas
    path('pagina-repartidor/', paginarepartidor, name='pagina-repartidor'),
    path('pagina-admin/', paginaadmin, name='pagina_administrador'),
    path('pagina_principal/', paginaprincipal, name='pagina_principal'),

    #Pedidos
    path('pedidos/', consultar_pedidos, name='pedidos'),
    path('ver_pedido/<int:pedido_id>/', ver_pedido),
    path('mis_pedidos/', mis_pedidos, name='mis_pedidos'),
    path('cancelar_pedido/<int:id_pedido>', cancelar_pedido, name='cancelar_pedido'),
    
    #Trivia
    path('trivias/', Trivias,name='trivias'),
    path('crear_trivia/', Crear_trivia,name='crear_trivia'),
    path('editar_trivia/<int:id_trivia>',Editar_Trivia,name="editar_trivia"),
    path('preguntas/<int:id_trivia>',Preguntas,name='preguntas'),
    path('crear_preguntas/<int:id_trivia>',Crear_Preguntas,name='crear_preguntas'),
    path('editar_pregunta/<int:id_pregunta>',Editar_Pregunta,name='editar_pregunta'),
    path('respuestas/<int:id_trivia>/<int:id_pregunta>',Respuestas,name='respuestas'),
    path('crear_respuestas/<int:id_trivia>/<int:id_respuesta>',Crear_Respuesta,name="crear_respuestas"),
    path('editar_respuestas/<int:id_trivia>/<int:id_respuesta>',Editar_Respuesta,name="editar_respuesta"),
    path('establecer_respuesta/<int:id_trivia>/<int:id_respuesta>',EstablecerCorrecta,name="establecer_respuesta"),
    path('activar_trivia/<int:id_trivia>',Activar_Trivia,name="activar_trivia"),
    path('desactivar_trivia/<int:id_trivia>',Desactiva_Trivia,name="desactivar_trivia"),
    path('mis_trivias',Mis_trivias,name="mis_trivias"),
    path('realizar_trivia/<int:id_trivia>',Responder_Trivia,name="realizar_trivia"),

    #Pagos
    path('mi_carrito/<int:usuario_id>',ver_carrito,name="mi_carrito"),
    path('agregar_a_carrito/<int:platillo_id>',agregar_a_carrito,name="agregar_a_carrito"),
    path('aumentar_cantidad/<int:pedido_carrito_id>',aumentar_cantidad,name='aumentar_cantidad'),
    path('disminuir_cantidad/<int:pedido_carrito_id>',disminuir_cantidad,name='disminuir_cantidad'),
    path('realizar_pedido/',realizar_pedido,name='realizar_pedido'),
    path('pago fracaso/',pagofracaso,name='pago fracaso'),
    path('pago exitoso/',pagoexitoso,name='pago exitoso'),

    #Usuario
    path('index usuario/', Index_Usuario, name='index_usuario'),
    path('usuarios/<int:emp_id>/', ver_usuario, name='ver_usuario'), 
    path('desactivar-usuario/<int:emp_id>/', desactivar_usuario, name='desactivar_usuario'),
    path('activar-usuario/<int:emp_id>/', activar_usuario, name='activar_usuario'),
    path('update_usuario/<int:emp_id>/', Update_Usuario),
    path('mi_cuenta',mi_cuenta,name='mi_cuenta'),
    path('update_mi_cuenta',Update_mi_cuenta,name="update_mi_cuenta"),
    path('updata_contraseña_mi_cuenta',actualizar_contraseña,name='actualizar_contraseña'),
    
    #Tomar pedido
    path('aceptar_pedido/<int:id_pedido>',aceptar_pedido,name='aceptar_pedido'),
    path('entregar_pedido/<int:id_pedido>',entregar_pedido,name='entregar_pedido'),

    path('dashboard/',dashboard,name="dashboard")#dashboad



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#para poder cargar la imagenes

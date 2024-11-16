from django.shortcuts import render, redirect, get_object_or_404
from .forms import CatalogoForm
from .models import Catalogo
from Platillo_app.models import Platillo
from Pedido_app.models import Pedido

def ingresarcatalogo(request):
    form = CatalogoForm()
    if request.method == 'POST':
        form = CatalogoForm(request.POST, request.FILES)  # Asegúrate de manejar archivos
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirigir a una URL después de guardar el formulario
    data = {'form': form, 'titulo': 'Agregar catálogo'}
    return render(request, 'ingresar_catalogo.html', data)


def paginaprincipal(request): 
    catalogos = Catalogo.objects.filter(estado='Activado').prefetch_related('platillos_set').all() 
    return render(request, 'pagina_principal.html', {'catalogos': catalogos})


def paginaadmin(request):
    catalogos = Catalogo.objects.prefetch_related('platillos_set').all()
    return render(request, 'pagina-admin.html', {'catalogos': catalogos})

def paginarepartidor(request):
    id = request.session['usuario_id']
    pedidos_generales = Pedido.objects.filter(estado = "activo")
    pedidos_aceptados = Pedido.objects.filter(repartidor__id = id, estado = "tomado")
    return render(request, 'pagina-repartidor.html',{'ped_generales':pedidos_generales,
                                                     'ped_aceptados':pedidos_aceptados})

def actualizarcatalogo(request, catalogo_id):
    catalogo = get_object_or_404(Catalogo, id=catalogo_id)
    if request.method == 'POST':
        form = CatalogoForm(request.POST, request.FILES, instance=catalogo)  # Vincula el formulario con el catálogo existente
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirigir a una URL después de actualizar el formulario
    else:
        form = CatalogoForm(instance=catalogo)
    data = {'form': form, 'titulo': 'Actualizar catálogo'}
    return render(request, 'ingresar_catalogo.html', data)



def asignar_platillo(request, catalogo_id):
    catalogo = get_object_or_404(Catalogo, id=catalogo_id)
    platillos = Platillo.objects.filter(catalogo__isnull=True)  # solo platillos sin catálogo asignado
    if request.method == 'POST':
        platillo_id = request.POST.get('platillo_id')
        platillo = get_object_or_404(Platillo, id=platillo_id)
        platillo.catalogo = catalogo
        platillo.save()
        return redirect('login')  # Redirige a la página de administración
    return render(request, 'asignar_platillo.html', {'catalogo': catalogo, 'platillos': platillos})

def ver_catalogo(request, catalogo_id):
    catalogo = get_object_or_404(Catalogo, id=catalogo_id)
    platillos_activados = catalogo.platillos_set.filter(estado='Activado')
    return render(request, 'ver_catalogo.html', {'catalogo': catalogo, 'platillos': platillos_activados})


def ver_catalogoadmin(request, catalogo_id):
    catalogo = get_object_or_404(Catalogo, id=catalogo_id)
    return render(request, 'ver_catalogo_admin.html', {'catalogo': catalogo})


def activar_catalogo(request, catalogo_id): 
    catalogo = get_object_or_404(Catalogo, id=catalogo_id) 
    catalogo.estado = 'Activado' 
    catalogo.save() 
    return redirect('pagina_administrador')

def desactivar_catalogo(request, catalogo_id):
    catalogo = get_object_or_404(Catalogo, id=catalogo_id)
    catalogo.estado = 'Desactivado'
    catalogo.save()
    return redirect('pagina_administrador')



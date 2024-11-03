from django.shortcuts import render, redirect, get_object_or_404
from .forms import CatalogoForm
from .models import Catalogo
from Platillo_app.models import Platillo

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
    catalogos = Catalogo.objects.prefetch_related('platillos_set').all()
    return render(request, 'pagina_principal.html', {'catalogos': catalogos})





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
    return render(request, 'ver_catalogo.html', {'catalogo': catalogo})


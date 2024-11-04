from django.shortcuts import render, redirect,get_object_or_404
from .forms import PlatilloForm,Platillo

def ingresarplatillo(request):
    if request.method == 'POST':
        form = PlatilloForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige a la página principal después de guardar
    else:
        form = PlatilloForm()
    return render(request, 'ingresar_platillo.html', {'form': form})

def activar_platillo(request, platillo_id):
    platillo = get_object_or_404(Platillo, id=platillo_id)
    platillo.estado = 'Activado'
    platillo.save()
    return redirect('ver_catalogo_admin', catalogo_id=platillo.catalogo.id)


def desactivar_platillo(request, platillo_id):
    platillo = get_object_or_404(Platillo, id=platillo_id)
    platillo.estado = 'Desactivado'
    platillo.save()
    return redirect('ver_catalogo_admin', catalogo_id=platillo.catalogo.id)


def actualizarplatillo(request, platillo_id):
    platillo = get_object_or_404(Platillo, id=platillo_id)
    if request.method == 'POST':
        form = PlatilloForm(request.POST, request.FILES, instance=platillo)  # Vincula el formulario con el platillo existente
        if form.is_valid():
            form.save()
            return redirect('ver_catalogo_admin', catalogo_id=platillo.catalogo.id)  # Redirigir a una URL después de actualizar el formulario
    else:
        form = PlatilloForm(instance=platillo)
    data = {'form': form, 'titulo': 'Actualizar platillo'}
    return render(request, 'ingresar_platillo.html', data)

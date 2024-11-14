from django.shortcuts import render, redirect,get_object_or_404
from .forms import PlatilloForm,Platillo

def ingresarplatillo(request):
    form = PlatilloForm()
    if request.method == 'POST':
        form = PlatilloForm(request.POST, request.FILES)  # Asegúrate de manejar archivos
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirigir a una URL después de guardar el formulario
    data = {'form': form, 'titulo': 'Agregar catálogo'}
    return render(request, 'ingresar_catalogo.html', data)


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

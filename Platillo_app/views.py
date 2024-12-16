from django.shortcuts import render, redirect,get_object_or_404
from .forms import PlatilloForm,Platillo

#permite el ingreso de un platillo desde la pagina
def ingresarplatillo(request):
    form = PlatilloForm()
    if request.method == 'POST':
        form = PlatilloForm(request.POST, request.FILES)  #  maneja archivos
        if form.is_valid():
            form.save()
            return redirect('pagina_administrador')  
    data = {'form': form, 'titulo': 'Agregar catálogo'}
    return render(request, 'ingresar_platillo.html', data)

#permite cambiar el estado de un platillo a activo
def activar_platillo(request, platillo_id):
    platillo = get_object_or_404(Platillo, id=platillo_id)
    platillo.estado = 'Activado'
    platillo.save()
    return redirect('ver_catalogo_admin', catalogo_id=platillo.catalogo.id)

#permite cambiar el estado de un platillo a inactivo
def desactivar_platillo(request, platillo_id):
    platillo = get_object_or_404(Platillo, id=platillo_id)
    platillo.estado = 'Desactivado'
    platillo.save()
    return redirect('ver_catalogo_admin', catalogo_id=platillo.catalogo.id)

#permite actualizar un platillo en la base de datos se detecta por la "id"
def actualizarplatillo(request, platillo_id):
    platillo = get_object_or_404(Platillo, id=platillo_id)
    if request.method == 'POST':
        form = PlatilloForm(request.POST, request.FILES, instance=platillo)  # Vincula el formulario con el platillo existente
        if form.is_valid():
            form.save()
            return redirect('ver_catalogo_admin', catalogo_id=platillo.catalogo.id) 
    else:
        form = PlatilloForm(instance=platillo)
    data = {'form': form, 'titulo': 'Actualizar platillo'}
    return render(request, 'ingresar_platillo.html', data)

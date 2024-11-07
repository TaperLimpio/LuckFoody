from django.shortcuts import render, redirect,get_object_or_404
from .forms import PlatilloForm,Platillo

def ingresarplatillo(request):
    form = PlatilloForm()
    if request.method == 'POST':
        form = PlatilloForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirigir al login después de crear la cuenta
    data = {'form': form, 'titulo': 'Crear cuenta'}
    return render(request, 'crear-cuenta.html', data)
    """
    if request.method == 'POST':
        formset = [PlatilloForm(request.POST, request.FILES, prefix=str(i)) for i in range(3)]
        valid_forms = []
        any_errors = False
        
        for form in formset:
            if any(form.data.get(form.prefix + '-' + field, '') for field in form.fields):
                if form.is_valid():
                    valid_forms.append(form)
                else:
                    any_errors = True

        if not any_errors:
            for form in valid_forms:
                form.save()
            return redirect('login')  # Redirige a la página principal después de guardar
    else:
        formset = [PlatilloForm(prefix=str(i)) for i in range(3)]
    return render(request, 'ingresar_platillo.html', {'formset': formset})
    """


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

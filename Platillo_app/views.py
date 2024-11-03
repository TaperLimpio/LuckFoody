from django.shortcuts import render, redirect
from .forms import PlatilloForm

def ingresarplatillo(request):
    if request.method == 'POST':
        form = PlatilloForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige a la página principal después de guardar
    else:
        form = PlatilloForm()
    return render(request, 'ingresar_platillo.html', {'form': form})


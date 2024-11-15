from django.shortcuts import render, redirect,get_object_or_404
from  Usuario_app.models import Usuario  # Asegúrate de que esta sea tu clase de usuario
from . import forms
from .forms import UsuarioForm,UsuarioAdminForm,Filtro

# Create your views here.
def login(request):
    if request.method == 'POST':
        nombre = request.POST.get('username')
        contraseña = request.POST.get('contraseña')  # Agregamos el campo fono
        usuario = Usuario.objects.filter(nombre=nombre, contraseña=contraseña).first()  # Usamos filter() y first()
        if usuario and usuario.estado == 'activo':
            request.session['usuario_id'] = usuario.id
            if usuario.tipo == 'usuario':
                return redirect('pagina_principal')  # Redirigir a la URL 'usuario'
            elif usuario.tipo == 'administrador':
                return redirect('pagina_administrador')  # Redirigir a la URL 'administrador'
            elif usuario.tipo=='repartidor':
                return redirect('repartidor')#lo mismo pero para el repartidor
        else:
            return render(request, 'login.html', {'error': 'Usuario inválido'})
    return render(request, 'login.html')

def crearcuenta(request):
    form = UsuarioForm()
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.estado='activo'
            usuario.tipo = 'usuario'  # Establecer el tipo a 'usuario' automáticamente
            usuario.save()
            return redirect('login')  # Redirigir al login después de crear la cuenta
    data = {'form': form, 'titulo': 'Crear cuenta'}
    return render(request, 'crear-cuenta.html', data)


def crearcuentaadmin(request):
    if request.method == 'POST':
        form = UsuarioAdminForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.estado='activo'
            form.save()
            return redirect('login')  # Redirigir al login después de crear la cuenta
    else:
        form = UsuarioAdminForm()
    data = {'form': form, 'titulo': 'Crear cuenta de administrador'}
    return render(request, 'crear-cuenta-admin.html', data)


def ver_usuario(request, emp_id):
    usuario = get_object_or_404(Usuario, id=emp_id)
    return render(request, 'view-usuario.html', {'usuario': usuario})


def Update_Usuario(request, emp_id):
    usuario = Usuario.objects.get(id=emp_id)
    form = UsuarioForm(instance=usuario)
    
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirigir al login después de actualizar
        
    data = {'form': form, 'titulo': 'Actualizar usuario'}
    return render(request, 'crear-cuenta.html', data)

def delete_usuario(request, emp_id):
    usuario = Usuario.objects.get(id=emp_id)
    if usuario:
        usuario.estado = 'inactivo'
        usuario.save()
    return redirect('login')

def Index_Usuario(request):
    filtro = Filtro(initial={'tipo':'----','estado':'----'})
    if request.method=="POST":
        filtro = Filtro(request.POST)
        if filtro.is_valid():
            Tipo = filtro.cleaned_data['tipo']
            Estado = filtro.cleaned_data['estado']
            print(Tipo)
            print(Estado)
            if (Tipo == 'Todo' and Estado == 'Todo'):
                print("todo")
                usuario = Usuario.objects.all()
                print(usuario)
            elif(Tipo != 'Todo' and Estado == 'Todo'):
                print("por tipo")
                usuario = Usuario.objects.filter(tipo = Tipo)
                print(usuario)
            elif(Estado != 'Todo'and Tipo == 'Todo'):
                print("por estado")
                usuario = Usuario.objects.filter(estado = Estado)
                print(usuario)
            else:
                print("por tipo y estado")
                usuario = Usuario.objects.filter(tipo = Tipo,estado = Estado)
    else:        
        usuario = Usuario.objects.all()
    data = {'usuario': usuario,'form':filtro}
    return render(request, 'usuarios.html', data)

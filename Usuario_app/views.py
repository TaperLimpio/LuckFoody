from django.shortcuts import render, redirect,get_object_or_404
from  Usuario_app.models import Usuario  # Asegúrate de que esta sea tu clase de usuario
from . import forms
from .forms import UsuarioForm,UsuarioAdminForm,Filtro
from django.contrib.auth.hashers import check_password,make_password

# Create your views here.

#es el login aqui dependiendo de tu tipo de usuario te enviara a una pagina especifica tambien recuerda tu id para poder hacer las operaciones
#respectivas dependiendo del tipo de usuario
def login(request):
    if request.method == 'POST':
        nombre = request.POST.get('username')
        contraseña = request.POST.get('contraseña')  # Agregamos el campo fono
        usuario = Usuario.objects.filter(nombre=nombre).first()  # Usamos filter() y first()
        if usuario and usuario.estado == 'activo':
            print("el usuario esta activo")
            print(contraseña)
            print(usuario.contraseña)
            print(check_password(contraseña,usuario.contraseña))
            if check_password(contraseña,usuario.contraseña):
                print("la contraseña se proceso correctamente")
                request.session['usuario_id'] = usuario.id
                if usuario.tipo == 'usuario':
                    return redirect('pagina_principal')  # Redirigir a la URL 'usuario'
                elif usuario.tipo == 'administrador':
                    return redirect('pagina_administrador')  # Redirigir a la URL 'administrador'
                elif usuario.tipo=='repartidor':
                    return redirect('pagina-repartidor')#lo mismo pero para el repartidor
            else:
                print("la contraseña no se proceso correctamente")
                return render(request, 'login.html', {'error': 'Usuario inválido'})
        else:
            print("el usuario no esta activo")
            return render(request, 'login.html', {'error': 'Usuario inválido'})
    return render(request, 'login.html')

#crea la cuenta del usuario siempre la creara con el tipo "usuario"(usuario=cliente)
def crearcuenta(request):
    form = UsuarioForm()
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.estado='activo'
            usuario.tipo = 'usuario'
            usuario.contraseña = make_password(usuario.contraseña)  # Establecer el tipo a 'usuario' automáticamente
            usuario.save()
            return redirect('login')  # Redirigir al login después de crear la cuenta
    data = {'form': form, 'titulo': 'Crear cuenta'}
    return render(request, 'crear-cuenta.html', data)

#le permite crear cuentas al administrador
def crearcuentaadmin(request):
    if request.method == 'POST':
        form = UsuarioAdminForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.estado='activo'
            usuario.contraseña = make_password(usuario.contraseña)
            form.save()
            return redirect('index_usuario')  # Redirigir al login después de crear la cuenta
    else:
        form = UsuarioAdminForm()
    data = {'form': form, 'titulo': 'Crear cuenta de administrador'}
    return render(request, 'crear-cuenta-admin.html', data)

#le permite ver sus datos al a todos los tipos usuario 
def ver_usuario(request, emp_id):
    usuario = get_object_or_404(Usuario, id=emp_id)
    tipo_usuario_consultor = Usuario.objects.get(id=request.session['usuario_id']).tipo
    return render(request, 'view-usuario.html', {'usuario': usuario,
                                                 'tipo_usuario_consultor':tipo_usuario_consultor})

def mi_cuenta(request):
    usuario = get_object_or_404(Usuario, id=request.session['usuario_id'])
    tipo_usuario_consultor = usuario.tipo
    return render(request, 'consultar-usuario.html', {'usuario': usuario,
                                                 'tipo_usuario_consultor':tipo_usuario_consultor})

#le permite actualizar a todos los tipos de usuarios
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

#cambia el estado del usuario a inactivo
def delete_usuario(request, emp_id):
    usuario = Usuario.objects.get(id=emp_id)
    if usuario:
        usuario.estado = 'inactivo'
        usuario.save()
    return redirect('login')

#permite ver una lista con todos los usuarios registrados tanto cliente,repartidores y administradores
def Index_Usuario(request):
    filtro = Filtro(initial={'tipo':'----','estado':'----'})
    ciudad_filtro = ""
    if request.method == "POST":
        filtro = Filtro(request.POST)
        ciudad_filtro = request.POST.get('ciudad')
        if filtro.is_valid():
            Tipo = filtro.cleaned_data['tipo']
            Estado = filtro.cleaned_data['estado']
            Ciudad = ciudad_filtro if ciudad_filtro else '----'
            
            usuario = Usuario.objects.all()
            
            if Tipo != '----':
                usuario = usuario.filter(tipo=Tipo)
            if Estado != '----':
                usuario = usuario.filter(estado=Estado)
            if Ciudad != '----':
                usuario = usuario.filter(ciudad=Ciudad)
            
    else:        
        usuario = Usuario.objects.all()
        
    data = {'usuario': usuario, 'form': filtro, 'ciudad_filtro': ciudad_filtro}
    return render(request, 'usuarios.html', data)




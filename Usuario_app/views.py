from django.shortcuts import render, redirect,get_object_or_404
from  Usuario_app.models import Usuario  # Asegúrate de que esta sea tu clase de usuario
from . import forms
from .forms import UsuarioForm,UsuarioAdminForm,Filtro,ActualizarUsuarioAdminForm
from .forms import ActualizarUsuarioForm
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
    form = UsuarioAdminForm()
    if request.method == 'POST':
        form = UsuarioAdminForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.estado='activo'
            usuario.contraseña = make_password(usuario.contraseña)
            form.save()
            return redirect('index_usuario')  # Redirigir al login después de crear la cuenta
    data = {'form': form, 'titulo': 'Crear cuenta de administrador'}
    return render(request, 'crear-cuenta-admin.html', data)

#le permite ver sus datos al a todos los tipos usuario 
def ver_usuario(request, emp_id):
    usuario = get_object_or_404(Usuario, id=emp_id)
    return render(request, 'consultar-usuario.html', {'usuario': usuario})

#permite ver los datos de la cuenta en la que estas registrada
def mi_cuenta(request):
    usuario = get_object_or_404(Usuario, id=request.session['usuario_id'])
    tipo_usuario_consultor = usuario.tipo
    return render(request, 'view-usuario.html', {'usuario': usuario,
                                                 'tipo_usuario_consultor':tipo_usuario_consultor})

def actualizar_contraseña(request):
    usuario = get_object_or_404(Usuario, id=request.session['usuario_id'])
    tipo_usuario_consultor = usuario.tipo
    data = {'tipo_usuario_consultor':tipo_usuario_consultor}
    if request.method == 'POST':
        contraseña_nueva = request.POST.get('contraseña_nueva')
        contraseña_nueva_2 = request.POST.get('contraseña_nueva_2')
        if contraseña_nueva != "" or contraseña_nueva_2 != "":
            if contraseña_nueva == contraseña_nueva_2:
                print(usuario.nombre)
                usuario.contraseña = make_password(contraseña_nueva)
                usuario.save()
                print(tipo_usuario_consultor)
                if tipo_usuario_consultor == "usuario":
                    return redirect('pagina_principal')
                elif tipo_usuario_consultor == "administrador":
                    return redirect('pagina_administrador')
                else:
                    return redirect('pagina-repartidor')
            else:
                data['error'] = 'Ingrese la misma nueva contraseña en los dos campos'
    
    return render(request, 'actualizar-contraseña.html',data)

#le permite actualizar a todos los tipos de usuarios
def Update_Usuario(request, emp_id):
    usuario = Usuario.objects.get(id=emp_id)
    form = ActualizarUsuarioAdminForm(instance=usuario)
    
    if request.method == "POST":
        form = ActualizarUsuarioAdminForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('ver_usuario', emp_id)  # Redirigir al login después de actualizar
        
    data = {'form': form, 'titulo': 'Actualizar usuario'}
    return render(request, 'actualizar-cuenta.html', data)

#le permite actualizar los datos de la cuenta registrada
def Update_mi_cuenta(request):
    usuario = get_object_or_404(Usuario, id=request.session['usuario_id'])
    tipo_usuario_consultor = usuario.tipo
    form = ActualizarUsuarioForm(instance=usuario)

    if request.method == "POST":
        form = ActualizarUsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('mi_cuenta')
        
    data = {'form':form,'tipo_usuario_consultor':tipo_usuario_consultor}
    return render(request, 'actualizar-mi-cuenta.html', data)

#cambia el estado del usuario a inactivo
def desactivar_usuario(request, emp_id):
    usuario = Usuario.objects.get(id=emp_id)
    if usuario:
        usuario.estado = 'inactivo'
        usuario.save()
    return redirect('ver_usuario',emp_id)

#cambia el estado del usuario a activo
def activar_usuario(request, emp_id):
    usuario = Usuario.objects.get(id=emp_id)
    if usuario:
        usuario.estado = 'activo'
        usuario.save()
    return redirect('ver_usuario',emp_id)

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




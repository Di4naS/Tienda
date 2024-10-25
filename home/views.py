from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Producto
from .forms import agregar_producto_form, login_form, register_form
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib import messages

# Función para verificar si el usuario es administrador
def es_administrador(user):
    return user.is_authenticated and user.is_staff

@login_required(login_url='/login/')
def vista_about(request):
    return render(request, 'about.html')

@login_required(login_url='/login/')
def vista_bio(request):
    return render(request, 'bio.html')

@login_required(login_url='/login/')
def vista_inicio(request):
    return render(request, 'inicio.html')

@login_required(login_url='/login/')
def vista_lista_producto(request):
    buscar = request.GET.get('buscar', '')  # Obtiene el parámetro de búsqueda de la solicitud GET.
    # Filtrar productos según el nombre buscado
    if buscar:
        lista = Producto.objects.filter(nombre__icontains=buscar)  # Filtrar por nombre
    else:
        lista = Producto.objects.all()  # Obtener todos los productos si no hay búsqueda

    # Comprobar si hay resultados
    no_resultados = not lista.exists()  # Variable para determinar si hay resultados

    return render(request, 'lista_producto.html', {'lista': lista, 'no_resultados': no_resultados, 'buscar': buscar})  
    # Pasa la lista de productos, la variable no_resultados, y el término de búsqueda

@login_required(login_url='/login/')
def vista_agregar_producto(request):
    if request.method == 'POST':
        formulario = agregar_producto_form(request.POST, request.FILES)
        if formulario.is_valid():
            prod = formulario.save(commit=False)
            prod.status = True
            prod.save()
            formulario.save_m2m()
            return redirect('vista_lista_producto')
    else:
        formulario = agregar_producto_form()
    return render(request, 'vista_agregar_producto.html', locals()) 

@login_required(login_url='/login/')
def vista_ver_producto(request, id_prod):
    p = Producto.objects.get(id=id_prod)
    return render(request, 'ver_producto.html', locals())

@login_required(login_url='/login/')
def vista_editar_producto(request, id_prod):
    prod = Producto.objects.get(id=id_prod)
    if request.method == "POST":
        formulario = agregar_producto_form(request.POST, request.FILES, instance=prod)
        if formulario.is_valid():
            prod = formulario.save()
            return redirect('vista_lista_producto')
    else:
        formulario = agregar_producto_form(instance=prod)
    return render(request, 'vista_agregar_producto.html', locals())

@login_required(login_url='/login/')
@user_passes_test(es_administrador, login_url='/lista_producto/')
def vista_eliminar_producto(request, id_prod):
    if request.method == "POST":
        prod = Producto.objects.get(id=id_prod)
        prod.delete()
        messages.success(request, "Producto eliminado correctamente.")
    else:
        messages.error(request, "No tienes permisos para realizar esta acción.")
    return redirect('vista_lista_producto')

# Login y Logout
def vista_login(request):
    if request.method == "POST":
        formulario = login_form(request.POST)
        if formulario.is_valid():
            usu = formulario.cleaned_data['usuario']
            cla = formulario.cleaned_data['clave']
            usuario = authenticate(username=usu, password=cla)
            if usuario is not None and usuario.is_active:
                login(request, usuario)
                return redirect('vista_inicio')
            else:
                msj = "Usuario o clave incorrectos"
    else:
        formulario = login_form()
    return render(request, 'login.html', locals())

def vista_logout(request):
    logout(request)
    return redirect('vista_login')

# Registro de usuarios
def vista_register(request):
    msj = ""
   # formulario = register_form()
    if request.method == 'POST':
        formulario = register_form(request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data['username']
            correo = formulario.cleaned_data['email']
            password_1 = formulario.cleaned_data['password_1']
            #password_2 = formulario.cleaned_data['password_2']
            #if password_1 == password_2:
            u = User.objects.create_user(username=usuario, email=correo, password=password_1)
            u.save()
            return render(request, 'thanks_for_register.html', locals())
        else:
                msj = "Por favor corrige los errores del formulario"
    else: 
        formulario = register_form()
        
    return render(request, 'register.html', locals())

@login_required(login_url='/login/')
def vista_perfil(request):
    return render(request, 'perfil.html', locals())

def vista_raiz(request):
    return redirect('vista_login') 



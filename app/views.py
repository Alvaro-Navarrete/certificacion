from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AnonymousUser, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.db import IntegrityError

def generar_menu(user: AbstractBaseUser | AnonymousUser):
    menu = []
    menu.append({'url':'/', 'nombre':'home'})
    if user != None and user.is_authenticated:
        menu.append({'url':'/opcion1/', 'nombre':'Opcion1'})
        menu.append({'url':'/opcion2/', 'nombre':'Opcion2'})
        menu.append({'url':'/#/', 'nombre':'Opcion3'})
    
    return menu

def home(request):
    return render(request, 'app/home.html', {'menu' : generar_menu(request.user)})

@login_required
def opcion1(request):
    
    user = User.objects.all()
    return render(request, 'app/opcion1.html', {'menu' : generar_menu(request.user), 'users': user})

@login_required
def opcion2(request):
    return render(request, 'app/opcion2.html', {'menu' : generar_menu(request.user)})




def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos')
        
    return render(request, 'app/home.html', {'menu' : generar_menu(request.user)})

# Funcion para creaer un usuario
def crear_usuario(request):
    try:
        if request.method == 'POST':
            
            username = request.POST['username']
            password = request.POST['password']
            first_name = request.POST['first-name']
            last_name = request.POST['last-name']
            email = request.POST['email']
            
            if not username or not password:
                raise ValueError('El nombre de usuario y la contraseña son obligatorios.')
            try:
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    email=email,
                    first_name=first_name,
                    last_name=last_name
                )
                user.save()
                
                messages.success(request, f'El usuario "{username}" se creó existosamente.')
                
                return redirect('home')
            
            except IntegrityError:
                messages.error(request, f'El usuario {username} ya existe.')
         
    except ValueError as e:
        messages.warning(request, str(e))
        
    except Exception:
        messages.error(request, 'Hubo un error inesperado.')
        
       
    return render(request, 'app/home.html', {'menu' : generar_menu(request.user)})


    
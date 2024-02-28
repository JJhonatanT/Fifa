from pyexpat.errors import messages
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import messages



def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Realiza la autenticación manualmente
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('admin:index')  # Redirige al panel de administración
        else:
            # Handle the case when authentication fails
            pass
            
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión finalizada')
    return redirect('login')

def register(request):
    if request.method == 'POST':
       
        username = request.POST.get('nombre-usuario')  
        email = request.POST.get('correo') 
        password = request.POST.get('contrasena') 
        confirm_password = request.POST.get('confirmar-contrasena') 

    
        if password != confirm_password:
         
            return render(request, 'register.html', {'error': 'Las contraseñas no coinciden'})

    
        user = User.objects.create_user(username=username, email=email, password=password)

     
        login(request, user)

      
        return redirect('login')

    return render(request, 'register.html')

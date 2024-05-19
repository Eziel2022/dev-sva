from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def home_view(request):
    return render(request, 'index.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
    
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('inicio')  
        else:
            return render(request, 'login.html', {'error': 'Correo electrónico o contraseña incorrectos.'})
    
    return render(request, 'login.html')


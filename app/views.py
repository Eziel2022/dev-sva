from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Notification
from .forms import NotificationForm
from .models import Event
from app.tasks import send_notification_email
from django.utils import timezone
from .tasks import send_notification_email
from datetime import timedelta

@login_required
def event_list(request):
    events = Event.objects.all()
    return render(request, 'eventlist.html', {'events': events})

@login_required
def notification_list(request):
    notifications = Notification.objects.filter(user=request.user)
    return render(request, 'notylist.html', {'notifications': notifications})

@login_required
def create_notification(request):
    if request.method == "POST":
        form = NotificationForm(request.POST)
        if form.is_valid():
            notification = form.save(commit=False)
            notification.user = request.user
            notification.save()
            
            send_time = notification.scheduled_for
            send_notification_email.apply_async((notification.id,), eta=send_time)
            
            return redirect('notification_list')
    else:
        form = NotificationForm()
    
    return render(request, 'notycreate.html', {'form': form})


def home_view(request):
    return render(request, 'app/index.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
    
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            next_page = request.GET.get('next', 'inicio')  
            return redirect(next_page)  
        else:
            return render(request, 'login.html', {'error': 'Correo electrónico o contraseña incorrectos.'})
    
    return render(request, 'login.html')


@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})

def logout_view(request):
    logout(request)
    return redirect('login')

def some_view(request):
    send_notification_email.delay('Asunto del Correo', 'Contenido del Correo', ['destinatario@example.com'])
    return render(request, 'template.html')

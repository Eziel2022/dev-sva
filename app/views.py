from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Notification, Alumno, Event
from .forms import NotificationForm, AlumnoForm, EventForm, EditarCorreoForm
from .tasks import send_notification_email
from django.utils import timezone
from django.urls import reverse
from django.db.models import Q

@login_required
def event_list(request):
    events = Event.objects.all()
    return render(request, 'list/eventlist.html', {'events': events})

@login_required
def notification_list(request):
    notifications = Notification.objects.filter(user=request.user)
    return render(request, 'list/notylist.html', {'notifications': notifications})

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_at = timezone.now()  
            event.save()
            print(f"Evento creado en: {event.created_at}")
            
            return redirect('inicio')
    else:
        form = EventForm()
    return render(request, 'create/create_event.html', {'form': form})


def home_view(request):
    events = Event.objects.all()
    return render(request, 'home.html', {'events': events})

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
            return render(request, 'log/login.html', {'error': 'Correo electrónico o contraseña incorrectos.'})
    
    return render(request, 'log/login.html')

@login_required
def profile_view(request):
    return render(request, 'log/profile.html', {'user': request.user})

def logout_view(request):
    logout(request)
    return redirect('login')

def some_view(request):
    send_notification_email.delay('Asunto del Correo', 'Contenido del Correo', ['destinatario@example.com'])
    return render(request, 'template.html')

def agregar_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_alumnos')  
    else:
        form = AlumnoForm()
    return render(request, 'add/agregar_alumno.html', {'form': form})

def lista_alumnos(request):
    alumnos = Alumno.objects.all()
    return render(request, 'list/lista_alumnos.html', {'alumnos': alumnos})

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.created_at = timezone.now()  
            event.save()
            print(f"Evento creado en: {event.created_at}")
            
            return redirect('inicio')
    else:
        form = EventForm()
    return render(request, 'create/create_event.html', {'form': form})

def delete_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('eventlist')
    return redirect('eventlist')  

@login_required
def student_list(request):
    query = request.GET.get('q')
    if query:
        alumnos = Alumno.objects.filter(
            Q(nombre__icontains=query) | 
            Q(apellido__icontains=query) | 
            Q(dni__icontains=query) |
            Q(numero_celular__icontains=query) |
            Q(correo_electronico__icontains=query)
        )
    else:
        alumnos = Alumno.objects.all()
    return render(request, 'list/lista_alumnos.html', {'alumnos': alumnos})

@login_required
def editar_correo(request, alumno_id):
    alumno = get_object_or_404(Alumno, id=alumno_id)
    
    if request.method == 'POST':
        form = EditarCorreoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = EditarCorreoForm(instance=alumno)
    
    return render(request, 'edits/editar_correo.html', {'form': form, 'alumno': alumno})

def events_view(request):
    return render(request, 'events.html')

def pasantias_view(request):
    return render(request, 'pasantias.html')

def becas_view(request):
    return render(request, 'becas.html')


def create_notification(request):
    return render(request, 'app/crear_notificacion.html')

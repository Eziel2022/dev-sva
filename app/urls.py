# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='inicio'),
    path('profile/', views.profile_view, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('notifications/', views.notification_list, name='notification_list'),
    path('notifications/create/', views.create_notification, name='notycreate'),  # Asegúrate de que esta línea esté presente
    path('events/', views.event_list, name='eventlist'),
    path('eventos/', views.events_view, name='events'),
    path('create_event/', views.create_event, name='create_event'),
    path('events/<int:event_id>/delete/', views.delete_event, name='delete_event'),
    path('agregar_alumno/', views.agregar_alumno, name='agregar_alumno'),
    path('lista_alumnos/', views.lista_alumnos, name='lista_alumnos'),
    path('students/', views.student_list, name='student_list'),
    path('alumno/<int:alumno_id>/editar_correo/', views.editar_correo, name='editar_correo'),
    path('pasantias/', views.pasantias_view, name='pasantias'),
    path('becas/', views.becas_view, name='becas'),
    
]

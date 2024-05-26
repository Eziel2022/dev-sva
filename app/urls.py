from django.urls import path
from . import views
from .views import (
    
    login_view, 
    home_view, 
    profile_view, 
    logout_view, 
    notification_list, 
    create_notification, 
    event_list,
    agregar_alumno, lista_alumnos, create_event, student_list
    
)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('home/', home_view, name='inicio'),
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),
    path('notifications/', notification_list, name='notification_list'),
    path('notifications/create/', create_notification, name='notycreate'),
    path('events/', event_list, name='eventlist'),
    path('agregar_alumno/', agregar_alumno, name='agregar_alumno'),
    path('lista_alumnos/', lista_alumnos, name='lista_alumnos'),
    path('create_event/', create_event, name='create_event'),
    path('events/<int:event_id>/delete/', views.delete_event, name='delete_event'),
    path('students/', views.student_list, name='student_list'),
]

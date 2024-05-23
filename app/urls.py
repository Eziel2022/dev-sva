from django.urls import path
from .views import (
    login_view, 
    home_view, 
    profile_view, 
    logout_view, 
    notification_list, 
    create_notification, 
    event_list
)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('home/', home_view, name='inicio'),
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),
    path('notifications/', notification_list, name='notification_list'),
    path('notifications/create/', create_notification, name='notycreate'),
    path('events/', event_list, name='eventlist'),
]

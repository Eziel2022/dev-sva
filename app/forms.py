from django import forms
from .models import Notification, Alumno, Event

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['title', 'message', 'scheduled_for']

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'dni', 'numero_celular', 'correo_electronico']
        labels = {
            'nombre': 'Name',
            'apellido': 'Last Name',
            'dni': 'DNI',
            'numero_celular': 'Phone Number',
            'correo_electronico': 'Email',
        }

    def clean_dni(self):
        dni = self.cleaned_data.get('dni')
        if Alumno.objects.filter(dni=dni).exists():
            raise forms.ValidationError('Este DNI ya está registrado.')
        return dni

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'image', 'event_type']


class EditarCorreoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['correo_electronico']
        widgets = {
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control'}),
        }


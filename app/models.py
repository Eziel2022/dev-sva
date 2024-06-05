from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email debe ser proporcionado')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser debe tener is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser debe tener is_superuser=True')

        return self.create_user(email, password, **extra_fields)

class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class Notification(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    scheduled_for = models.DateTimeField()
    sent = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=10, unique=True)  
    numero_celular = models.CharField(max_length=15)
    correo_electronico = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='events/', default='default.jpg')
    created_at = models.DateTimeField(default=timezone.now)  
    
    def __str__(self):
        return self.title


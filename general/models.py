from django.db import models

# Create your models here.

class UserModel(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=12)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    #image = models.ImageField(upload_to='fotos/')
    #created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class LoginModel(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=150)



class TrabajadorModel(models.Model):
    id = models.IntegerField(primary_key=True)
    matricula = models.CharField(max_length=20, null=True, blank=True)
    nombre = models.CharField(max_length=250, null=True, blank=True)
    categoria = models.CharField(max_length=250, null=True, blank=True)
    uadscripcion = models.CharField(max_length=250, null=True, blank=True)
    turno = models.CharField(max_length=150, null=True, blank=True)
    correo = models.CharField(max_length=150, null=True, blank=True)
    telefono = models.CharField(max_length=100, null=True, blank=True)
    verificar = models.CharField(max_length=100, null=True, blank=True)
    #created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.matricula



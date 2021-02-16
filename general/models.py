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
    """nombre = models.CharField(max_length=20)
    domicilio = models.CharField(max_length=20)
    colonia = models.CharField(max_length=20)
    municipio = models.CharField(max_length=20)
    cp = models.CharField(max_length=20)
    localidad = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    correo = models.CharField(max_length=20)
    lugar_nac = models.CharField(max_length=20)
    f_dia = models.CharField(max_length=20)
    f_mes = models.CharField(max_length=20)
    f_anio = models.CharField(max_length=20)
    nss = models.CharField(max_length=20)
    rfc = models.CharField(max_length=20)
    e_c = models.CharField(max_length=20)
    curp = models.CharField(max_length=20)
    categoria = models.CharField(max_length=20)
    matricula = models.CharField(max_length=20)
    sueldo = models.CharField(max_length=20)
    uadscripcion = models.CharField(max_length=20)
    f_ingreso = models.CharField(max_length=20)
    a_a = models.CharField()
    a_q = models.CharField()
    a_d = models.CharField()
    q_proc = models.CharField()"""

    matricula = models.CharField(max_length=20)
    nombre = models.CharField(max_length=250)
    categoria = models.CharField(max_length=250)
    uadscripcion = models.CharField(max_length=250)
    turno = models.CharField(max_length=150)
    #telefono = models.CharField(max_length=70)
    correo = models.CharField(max_length=150)
    telefono = models.CharField(max_length=100)
    #created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.matricula



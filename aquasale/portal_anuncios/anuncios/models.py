from django.db import models

# Create your models here.

class Tipo(models.Model):
    nombre = models.CharField(max_length=25)
    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=25)
    def __str__(self):
        return self.nombre

class Usuario (models.Model):
    nombre = models.CharField(max_length = 150)
    clave = models.CharField(max_length = 150)
    email = models.CharField(max_length = 150, unique=True) #el email tiene que ser único.

    def __str__(self):
        return self.email

class Anuncio(models.Model):
    fecha = models.CharField(max_length=50)
    tipo = models.ForeignKey(Tipo,on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=3000,blank=True)
    precio = models.FloatField(default=0)
    nomyapell = models.CharField(max_length=100, verbose_name="Nombre y apellidos")
    foto = models.ImageField (upload_to="fotografias", null=True)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo





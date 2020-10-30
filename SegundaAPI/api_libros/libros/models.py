from django.db import models

# Create your models here.

class Libro (models.Model):
    titulo = models.CharField(max_length=1000, blank=False, default='')
    genero = models.CharField(max_length=200, blank=False, default='')
    autor = models.CharField(max_length=70, blank=False, default='')
    tapa_dura = models.BooleanField(default=False)
    

class Persona (models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField ('Nombre',max_length = 100)
    apellido = models.CharField ('Apellido',max_length = 200)
    
    def __str__(self):
        return '{0},{1}'.format (self.apellido,self.nombre)
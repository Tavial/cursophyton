from django.db import models

# Create your models here.

class Personaje (models.Model):
    nombre = models.CharField (max_length=128)
    
    # Este campo no lo ponemos obligatorio ya que, por ej: Tanos no tiene nombre real
    nombre_real = models.CharField (max_length=128)
    
    imagen = models.ImageField()
    
    descripcion = models.TextField()

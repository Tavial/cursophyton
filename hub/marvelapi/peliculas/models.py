from django.db import models

# Create your models here.


class Pelicula (models.Model):
    titulo = models.CharField (max_length=128)
    
    anyo = models.DateField () 
    
    sinopsis = models.TextField ()
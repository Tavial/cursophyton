from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

#importamos el modelo personaje
from personajes.models import Personaje
#importamos el serializador
from personajes.serializers import PersonajeSerializer

class PersonajesViewSet (viewsets.ModelViewSet):
    # Traemos todos los personajes de nuestra base de datos
    queryset = Personaje.objects.all()
    #Le especificamos como quiero convertirlo a un archivo JSON (ya lo definimos en serializer)
    serializer_class = PersonajeSerializer
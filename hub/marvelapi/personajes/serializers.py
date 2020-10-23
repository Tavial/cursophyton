#importamos los serializadores
from rest_framework import serializers

#Tenemos que importar la clase cuyos objetos vamos a serializar
from personajes.models import Personaje

#creamos el serializador de nuestro personaje. 

class PersonajeSerializer (serializers.ModelSerializer):
    class Meta: #tiene los metadatos de la clase que vamos a utilizar y de los campos que vamos a 
                #serializar
        model = Personaje #Convertirá un objeto personaje en un archivo Json que podamos leer
        # le decimos qué campos queremos serializar (los que queremos que aparezcan en el archivo Json)
        fields = ("id","nombre","nombre_real","imagen","descripcion")
        
from django.shortcuts import render

# Create your views here.

from django.http.response import JsonResponse


from rest_framework import status
from rest_framework.parsers import JSONParser 
 
from .models import Libro
from .serializers import LibroSerializer
from rest_framework.decorators import api_view



@api_view(["GET"])


def bienvenido (request):
    contexto = {"mensaje": "Bienvenido a mi libreria!"}
    return JsonResponse(contexto)

# Obtenemos todos los libros
@api_view(["GET"])

def obtenerLibros(request):
    libros = Libro.objects.all()
    serializer = LibroSerializer(libros, many=True)
    return JsonResponse({'libros': serializer.data}, safe=False, status=status.HTTP_200_OK)


# Obtenemos un libro por ID
@api_view(["GET"])

def obtenerLibro (request, id_libro):
    try: 
        libro = Libro.objects.get(pk=id_libro) 
        libro_serializer = LibroSerializer(libro) # serializamos el libro que obtenemos
        return JsonResponse(libro_serializer.data) # mostramos el libro obtenido
    except Libro.DoesNotExist: 
        return JsonResponse({'mensaje': 'El libro solicitado no existe'}, status=status.HTTP_404_NOT_FOUND) 
 
    

# Añadimos un libro
@api_view(["POST"])
def nuevoLibro (request):
    #se parsea el request para obtener un diccionario con los datos de ese JSON
    libro_data = JSONParser().parse(request) 
    print (libro_data)
    libro_serializer = LibroSerializer (data=libro_data)
    if libro_serializer.is_valid():
        libro_serializer.save()
        return JsonResponse (libro_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse (libro_serializer.errors, status = status.HTTP_400_BAD_REQUEST)


#actualiza un libro por ID
@api_view(["PUT"])
def actualizarLibro (request, id_libro):
    try: 
        libro = Libro.objects.get(pk=id_libro) 
        libro_data = JSONParser().parse(request) 
        libro_serializer = LibroSerializer(libro, data=libro_data) 
        if libro_serializer.is_valid(): 
            libro_serializer.save() 
            return JsonResponse(libro_serializer.data) 
        return JsonResponse(libro_serializer.errors, status=status.HTTP_400_BAD_REQUEST)      
    except Libro.DoesNotExist: 
        return JsonResponse({'mensaje': 'El libro no existe'}, status=status.HTTP_404_NOT_FOUND) 

@api_view(["DELETE"])
def borrarLibro (request, id_libro):
    try: 
        libro = Libro.objects.get(pk=id_libro) 
        libro.delete() 
        return JsonResponse({'mensaje': 'El libro fue eliminado con éxito!'}, status=status.HTTP_204_NO_CONTENT)
        
    except Libro.DoesNotExist: 
        return JsonResponse({'mensaje': 'El libro no existe'}, status=status.HTTP_404_NOT_FOUND) 

@api_view(["DELETE"])
def borrarTodo (request):
    contador = Libro.objects.all().delete()
    return JsonResponse({'mensaje': '{} libros se han borrado correctamente'.format(contador[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view (['GET'])
def listaTapaDura(request):
    # Obtiene todos los libros de tapa dura (por condición)
    libros = Libro.objects.filter(tapa_dura=True)
    libros_serializer = LibroSerializer(libros, many=True)
    return JsonResponse(libros_serializer.data, safe=False)


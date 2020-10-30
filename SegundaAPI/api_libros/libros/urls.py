from django.urls import path
from . import views

urlpatterns = [
    path('api/bienvenida',views.bienvenido),
    path('api/libros',views.obtenerLibros),
    path('api/libros/<int:id_libro>',views.obtenerLibro),
    path('api/libros/nuevo-libro',views.nuevoLibro),
    path('api/libros/actualizar-libro/<int:id_libro>',views.actualizarLibro),
    path('api/libros/borrar-libro/<int:id_libro>',views.borrarLibro),
    path('api/libros/borrar-todo',views.borrarTodo),
    path('api/libros/libros-tapa-dura',views.listaTapaDura),
]

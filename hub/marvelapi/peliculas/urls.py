#importamos el include para generar las urls de las vistas
from django.urls import include,path

#Importamos la clase DefaultRouter de la que heredará nuestro objeto router
from rest_framework.routers import DefaultRouter

#importamos la vista donde solicitamos que se muestren todos los personajes
from peliculas.views import PeliculasViewSet

router = DefaultRouter ()

router.register("peliculas",PeliculasViewSet)

urlpatterns = [
    path('',include(router.urls)),

]
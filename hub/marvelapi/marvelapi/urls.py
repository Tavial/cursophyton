"""marvelapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#importamos el include para generar las urls de las vistas
from django.urls import include


"""
#Importamos la clase DefaultRouter de la que heredará nuestro objeto router
from rest_framework.routers import DefaultRouter

#importamos la vista donde solicitamos que se muestren todos los personajes
from personajes.views import PersonajesViewSet
from peliculas.views import PeliculasViewSet

# un router recibe nombres (en este caso personajes) y una vista y automáticamente genera las 
#urls para esa vista
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('peliculas/',include("peliculas.urls")),
    path('personajes/',include("personajes.urls")),
]


'''

router = DefaultRouter ()

router.register("peliculas",PeliculasViewSet)
urlpatterns = router.urls
router.register("personajes",PersonajesViewSet)
urlpatterns = router.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('',include(router.urls)),
]
'''

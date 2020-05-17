# Equivalente al @app.route de Django
# hacemos las siguientes importaciones
from django.urls import path # la podemos traer del urls.py del base
# ahora necesitamos traer las funciones de las rutas. Estas funciones las hemos creado en el
# archivo views_anuncios.py por lo que lo tenemos que importar:
from . import views_anuncios, views_usuarios
# aquí ponemos todas las rutas que debemos tener y qué función se ejecuta en cada una.
# Esto es como cuando poníamos en Flask lo de @app.route("/")
urlpatterns = [
    path("",views_anuncios.inicio),
    path("registrar-anuncio",views_anuncios.registrar_anuncio),
    path("guardar-anuncio",views_anuncios.guardar_anuncio),
    path("guardar-anuncio/registro-ok",views_anuncios.registro_ok),
    path("registrar-usuario",views_usuarios.registrar_usuario),
    path("guardar-usuario",views_usuarios.guardar_usuario),
    path("guardar-usuario/usuario-ok",views_usuarios.usuario_ok),
    path("login-usuario",views_usuarios.login_usuario),
    path("identificar-usuario",views_usuarios.identificar_usuario),
    path("logout-usuario",views_usuarios.logout_usuario),
    path("tus-anuncios",views_anuncios.tus_anuncios),
    path("borrar-anuncio",views_anuncios.borrar_anuncio),
    path("editar-anuncio",views_anuncios.editar_anuncio),
    path("guardar-cambios-anuncio",views_anuncios.guardar_cambios_anuncio),
    path("guardar-cambios-anuncio/edicion-ok",views_anuncios.edicion_ok),
]

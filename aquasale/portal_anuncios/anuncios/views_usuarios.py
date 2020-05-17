from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models
from anuncios.mis_clases.clase_fecha import Fecha
from anuncios.mis_clases.clase_validador import Validador
from anuncios import views_anuncios

# Aquí creamos las funciones. Similar al flask_app cuando creábamos las funciones para cada
# @app.route pero solo para anuncios.

def registrar_usuario (request):
    return render (request,"formulario-registro-usuario.html")

def guardar_usuario (request):
    nombre_insertado = request.POST["nombre"]
    # Tendremos que asegurarnos que el email no tenga espacios o mayúsculas y minúsculas como única diferncia con alguno que ya tengamos.
    email_insertado = request.POST["email"].lower().strip()
    clave_insertada = request.POST["clave"]

    # Hacemos la doble validación por código con ayuda de la clase Validador

    validador = Validador()

    nombre_valido = validador.nombreApellidos(str(nombre_insertado))
    email_valido = validador.email(str(email_insertado))
    clave_valida = validador.noVacio(str(clave_insertada))

    if nombre_valido and email_valido and clave_valida:
        # Vamos a comprobar que en la base de datos no hay otro email igual que ese.
        # Para ello compruebo que en la base de datos no hay ningún usuario con ese email.
        lista_email = models.Usuario.objects.filter(email = email_insertado)

        # No puedo poner directamente en el response el resultado. Tengo que indicarle que el elemento de valor, sacamos su nombre.
        #return HttpResponse ("Respuesta:"+lista_email[0].nombre)

        if len(lista_email) == 1:  #ya hay un usuario con ese email
            context = {
                "error_email": "Ya existe un usuario con ese email"
            }
            return render(request,"formulario-registro-usuario.html",context)
        else:  # si no hay ningún usuario con ese email inserto el nuevo usuario en la base de datos.
            usuario = models.Usuario(nombre=nombre_insertado, email = email_insertado, clave = clave_insertada)
            usuario.save()
            return redirect ("guardar-usuario/usuario-ok")
    else: # algo no ha ido bien. Se han saltado la seguridad HTML.
        return render(request, "registro-ko.html")

def usuario_ok (request):
    return render(request, "usuario-ok.html")

def login_usuario (request):
    return render (request, "login-usuario.html")

def identificar_usuario (request):
    email_insertado = request.POST["email"].lower().strip()
    clave_insertada = request.POST["clave"]

    # Hacemos la doble validación por código con ayuda de la clase Validador

    validador = Validador()

    email_valido = validador.email(str(email_insertado))

    if email_valido:
        # Buscamos en la base de datos el usuario que coincida con el login.
        lista_usuarios =models.Usuario.objects.filter (email = email_insertado, clave = clave_insertada)

        if len(lista_usuarios) == 0: #Si la longitud de la lista devuelta en la consulta es 0 es que el usuario no está registrado en el portal
            context = {
                "error_login": "email o contraseña incorrecta"
            }
            return render (request,"login-usuario.html",context)
        else: # El usuario está registrado
            usuario = lista_usuarios [0] #Es el único registro que nos puede devolver por lo que el campo 0 sabemos que es el nombre
            request.session["id_usuario"] = usuario.id # Django por defecto guarda en tabla Django Session la información del usuario que entra en sesión.
            #Tenemos que ponerle en la sesión la id. Django no permite guardar todo el objeto usuario.
            context = {
                "nombre":usuario.nombre
            }
            return render (request,"login-ok.html",context)
    else: # algo no ha ido bien. Se han saltado la seguridad HTML.
        return render(request, "registro-ko.html")

def logout_usuario (request):
    request.session.clear()
    return views_anuncios.inicio(request) # para que vuelva a listar los anuncios paso la ejecución a la función inicio.


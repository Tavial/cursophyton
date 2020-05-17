from django.http import HttpResponse
from django.shortcuts import render, redirect
from . import models
from anuncios.mis_clases.clase_fecha import Fecha
from anuncios.mis_clases.clase_validador import Validador
from django.conf import settings
import os


# Aquí creamos las funciones. Similar al flask_app cuando creábamos las funciones para cada
# @app.route pero solo para anuncios.

def inicio (request): # las funciones de Django tienen que pedir un request. Tienen que dar un resultado.
    # return HttpResponse ("Portal AquaSale. Página de inicio")
    ####  BUSCADOR  #####

    tipos = models.Tipo.objects.order_by("id")  # Recogemos los tipos (agua dulce, agua salada) de nuestra tabla Tipo

    categorias = models.Categoria.objects.order_by("id")  # Recogemos las categorías (peces, invertebrados, plantas) de nuestra tabla Categoria
    buscador = ""

    # Miramos si el usuario nos ha puesto en el buscador un título de anuncio
    if "buscador" not in request.GET:
        if "titulo" in request.GET: # obtenemos el valor del input text del index.html si hay algo
            buscador = request.GET["titulo"]
    else:
        buscador = request.GET["buscador"]

    # Recogemos de base de datos todos los anuncios ordenados por id de menor a mayor (fijarse en el menos de -id)
    # Cuando nos de los anuncios nos de también las categorías y tipos, porque si las pedimos después,
    # Django haría una SELECT por cada categoria y cada tipo de cada anuncio

    # Django emplea una ejecución diferida de la sql, hasta que no usemos
    # realmente un resultado, podemos agregar filtrados sobre el mismo.
    lista_anuncios = models.Anuncio.objects.filter(titulo__contains = buscador).order_by("-id").prefetch_related('tipo','categoria','usuario')
    # diccionario donde metemos todo lo que queremos que le llegue a la plantilla index.html

    #tomamos los valores que el usuario selecciona en el buscador de tipos y categorias. Si no ha escogido ninguno ponemos por defecto Todos
    if "tipo_elegido" not in request.GET:
        if "tipo" in request.GET:
            tipo_elegido = request.GET["tipo"]
        else:
            tipo_elegido = "-1"
    else:
        tipo_elegido=request.GET["tipo_elegido"]

    if "categoria_elegida" not in request.GET:
        if "categoria" in request.GET:
            categoria_elegida = request.GET["categoria"]
        else:
            categoria_elegida = "-1"
    else:
        categoria_elegida = request.GET["categoria_elegida"]

    if tipo_elegido =="-1":
        if categoria_elegida == "-1":
            lista_anuncios = lista_anuncios
        else: #categoria elegida distinta de Todos
            lista_anuncios = lista_anuncios.filter(categoria_id=categoria_elegida)
    else:
        if categoria_elegida == "-1":
            lista_anuncios = lista_anuncios.filter(tipo_id=tipo_elegido)
        else: #categoria elegida distinta de Todos
            lista_anuncios = lista_anuncios.filter(categoria_id=categoria_elegida, tipo_id=tipo_elegido)

    #### PAGINACION  ####
    total_anuncios = lista_anuncios.count
    resultados_por_pagina = 5 #queremos sacar resultados de 5 en 5
    comienzo = 0

    if "comienzo" in request.GET: #con esto vemos si han pulsado el enlace
        comienzo = int (request.GET["comienzo"])
    siguiente = comienzo + resultados_por_pagina
    anterior = comienzo - resultados_por_pagina
    lista_anuncios = lista_anuncios[comienzo:comienzo+resultados_por_pagina] #así decimos que solo coja los 5 primeros

    # sacamos el total de anuncios que hay en la base de datos:
    #total_anuncios=models.Anuncio.objects.count()

    #########################
    context ={
                "anuncios":lista_anuncios,
                "buscador":buscador,
                "categoria_elegida":int(categoria_elegida),
                "tipo_elegido":int(tipo_elegido),
                "tipos":tipos,
                "categorias":categorias,
                "siguiente": siguiente,
                "anterior": anterior,
                "total_anuncios":total_anuncios
    }
    return render (request,"index.html",context)

def registrar_anuncio (request):
    tipos = models.Tipo.objects.order_by("id") #Recogemos los tipos (agua dulce, agua salada) de nuestra tabla Tipo
    categorias = models.Categoria.objects.order_by("id") #Recogemos las categorías (peces, invertebrados, plantas) de nuestra tabla Categoria
    # aquí montamos el diccionario que se le va a pasar al html del formulario para que pueda mostrar los tipos y las categorías en el select
    context = {
        "tipos":tipos,
        "categorias":categorias
    }
    return render (request,"formulario-registro-anuncio.html",context)

def registro_ok (request):
    return render (request,"registro-ok.html")

def guardar_anuncio (request):
    #cogemos el valor de los campos del formulario:
    id_tipo_elegido = request.POST["radio"]
    id_categoria_elegida = request.POST["categoria"]
    titulo_elegido = request.POST["titulo"]
    descripcion_elegida = request.POST["descripcion"]
    precio_elegido = request.POST["precio"].replace (",",".")
    nomyapell_elegidos = request.POST["nomyapell"]
    foto_elegida = request.FILES.get("foto")

    # Hacemos la doble validación por código con ayuda de la clase Validador
    validador = Validador()
    titulo_valido = validador.noVacio(str(titulo_elegido))
    precio_valido = validador.numReal(str(precio_elegido))
    nomyapell_validos = validador.nombreApellidos(str(nomyapell_elegidos))


    if titulo_valido and precio_valido and nomyapell_validos: # si todo correcto se realiza el registro

        fechaActual = Fecha ()
        fecha_hoy= fechaActual.mostrarFecha()
        tipo_elegido = models.Tipo.objects.get(pk = id_tipo_elegido) # tengo que sacar el tipo de id_tipo_elegido
        # quiero que me de el tipo cuyo id sea id_tipo_elegido que es el seleccionado en el formulario

        categoria_elegida = models.Categoria.objects.get(pk = id_categoria_elegida)  # tengo que sacar la categoría de id_categoria_elegida
        # quiero que me de la categoria cuyo id sea id_categoria_elegida que es la seleccionada en el formulario
        # request.session["id_usuario"] es quien va a a contener el id del usuario de la sesión.
        # Fue el "sello" que le pusimos en la función identificar-usuario cuando el usuario se logó
        usuario_actual = models.Usuario.objects.get(pk=request.session["id_usuario"])

        #también se podría añadir al objeto "por partes", ejemplo: anuncio.usuario=usuario_actual
        anuncio = models.Anuncio (fecha = fecha_hoy, tipo = tipo_elegido, categoria = categoria_elegida, titulo = titulo_elegido, descripcion = descripcion_elegida, precio = precio_elegido, nomyapell = nomyapell_elegidos, foto =foto_elegida, usuario = usuario_actual)
        anuncio.save ()
        return redirect ("guardar-anuncio/registro-ok")
    else: # algo no ha ido bien. Se han saltado la seguridad HTML.
        return render (request,"registro-ko.html")

def tus_anuncios (request):
    # vamos a pedir todos los anuncios del usuario que tenga el id de sesión actual.
    # obtenemos el usuario.
    usuario_actual = models.Usuario.objects.get(pk=request.session["id_usuario"])
    # obtenemos el listado.
    #listado_anuncios = models.Anuncio.objects.order_by ("-id").filter(usuario = usuario_actual)

    ####  BUSCADOR  #####

    tipos = models.Tipo.objects.order_by("id")  # Recogemos los tipos (agua dulce, agua salada) de nuestra tabla Tipo

    categorias = models.Categoria.objects.order_by(
        "id")  # Recogemos las categorías (peces, invertebrados, plantas) de nuestra tabla Categoria
    buscador = ""

    # Miramos si el usuario nos ha puesto en el buscador un título de anuncio
    if "buscador" not in request.GET:
        if "titulo" in request.GET:  # obtenemos el valor del input text del index.html si hay algo
            buscador = request.GET["titulo"]
    else:
        buscador = request.GET["buscador"]

    # Recogemos de base de datos todos los anuncios ordenados por id de menor a mayor (fijarse en el menos de -id)
    # Cuando nos de los anuncios nos de también las categorías y tipos, porque si las pedimos después,
    # Django haría una SELECT por cada categoria y cada tipo de cada anuncio

    # Django emplea una ejecución diferida de la sql, hasta que no usemos
    # realmente un resultado, podemos agregar filtrados sobre el mismo.
    # listado_anuncios = models.Anuncio.objects.order_by ("-id").filter(usuario = usuario_actual)
    lista_anuncios = models.Anuncio.objects.filter(titulo__contains=buscador,usuario = usuario_actual).order_by("-id").prefetch_related('tipo','categoria','usuario')

    # tomamos los valores que el usuario selecciona en el buscador de tipos y categorias. Si no ha escogido ninguno ponemos por defecto Todos
    if "tipo_elegido" not in request.GET:
        if "tipo" in request.GET:
            tipo_elegido = request.GET["tipo"]
        else:
            tipo_elegido = "-1"
    else:
        tipo_elegido = request.GET["tipo_elegido"]

    if "categoria_elegida" not in request.GET:
        if "categoria" in request.GET:
            categoria_elegida = request.GET["categoria"]
        else:
            categoria_elegida = "-1"
    else:
        categoria_elegida = request.GET["categoria_elegida"]

    if tipo_elegido == "-1":
        if categoria_elegida == "-1":
            lista_anuncios = lista_anuncios
        else:  # categoria elegida distinta de Todos
            lista_anuncios = lista_anuncios.filter(categoria_id=categoria_elegida)
    else:
        if categoria_elegida == "-1":
            lista_anuncios = lista_anuncios.filter(tipo_id=tipo_elegido)
        else:  # categoria elegida distinta de Todos
            lista_anuncios = lista_anuncios.filter(categoria_id=categoria_elegida, tipo_id=tipo_elegido)

    #### PAGINACION  ####
    total_anuncios = lista_anuncios.count
    resultados_por_pagina = 5  # queremos sacar resultados de 5 en 5
    comienzo = 0

    if "comienzo" in request.GET:  # con esto vemos si han pulsado el enlace
        comienzo = int(request.GET["comienzo"])
    siguiente = comienzo + resultados_por_pagina
    anterior = comienzo - resultados_por_pagina
    lista_anuncios = lista_anuncios[comienzo:comienzo + resultados_por_pagina]  # así decimos que solo coja los 5 primeros

    context = {
        "usuario": usuario_actual,
        "anuncios":lista_anuncios,
        "buscador": buscador,
        "categoria_elegida": int(categoria_elegida),
        "tipo_elegido": int(tipo_elegido),
        "tipos": tipos,
        "categorias": categorias,
        "siguiente": siguiente,
        "anterior": anterior,
        "total_anuncios": total_anuncios
    }
    return render (request,"anuncios-usuario.html",context)

def borrar_anuncio (request):
    # cojo el id que llega por la interrogación del enlace Borrar
    id = request.GET["id"]
    elemento = models.Anuncio.objects.get(pk=id)

    if elemento.foto:
        os.remove(settings.BASE_DIR + elemento.foto.url)

    # Borra el anuncio
    models.Anuncio.objects.get(pk=id).delete()
    return tus_anuncios(request)

def editar_anuncio (request):
    id = request.GET["id"]
    # Tengo que mostrar un formulario con el anuncio del usuario que se quiere editar.
    anuncio_a_editar = models.Anuncio.objects.get(pk = id)
    # pido las categorias
    tipos = models.Tipo.objects.order_by("id")  # Recogemos los tipos (agua dulce, agua salada) de nuestra tabla Tipo
    categorias = models.Categoria.objects.order_by("id")  # Recogemos las categorías (peces, invertebrados, plantas) de nuestra tabla Categoria
    context = {
        "anuncio":anuncio_a_editar,
        "tipos":tipos,
        "categorias":categorias
    }
    return render (request,"editar-anuncio.html",context)

def guardar_cambios_anuncio (request):
    #cojo el anuncio del que quiero guardar cambios del campo hidden y el resto de los campos.
    id_anuncio_elegido = request.POST["id_anuncio"]
    id_tipo_elegido = request.POST["radio"]
    id_categoria_elegida = request.POST["categoria"]
    titulo_elegido = request.POST["titulo"]
    descripcion_elegida = request.POST["descripcion"]
    precio_elegido = request.POST["precio"].replace (",",".")
    nomyapell_elegidos = request.POST["nomyapell"]
    foto_elegida = request.FILES.get("foto")

    # Hacemos la doble validación por código con ayuda de la clase Validador
    validador = Validador()
    titulo_valido = validador.noVacio(str(titulo_elegido))
    precio_valido = validador.numReal(str(precio_elegido))
    nomyapell_validos = validador.nombreApellidos(str(nomyapell_elegidos))

    if titulo_valido and precio_valido and nomyapell_validos:  # si todo correcto se realiza el registro
        fechaActual = Fecha()
        fecha_hoy = fechaActual.mostrarFecha()
        # quiero que me de el tipo cuyo id sea id_tipo_elegido que es el seleccionado en el formulario
        tipo_elegido = models.Tipo.objects.get(pk=id_tipo_elegido)  # tengo que sacar el tipo de id_tipo_elegido

        # quiero que me de la categoria cuyo id sea id_categoria_elegida que es la seleccionada en el formulario
        categoria_elegida = models.Categoria.objects.get(pk=id_categoria_elegida)  # tengo que sacar la categoría de id_categoria_elegida

        # request.session["id_usuario"] es quien va a a contener el id del usuario de la sesión.
        # Fue el "sello" que le pusimos en la función identificar-usuario cuando el usuario se logó
        usuario_actual = models.Usuario.objects.get(pk=request.session["id_usuario"])

        #si no cambiamos imagen, nos quedaremos con la imagen que teníamos
        anuncio_a_editar = models.Anuncio.objects.get(pk=id_anuncio_elegido)

        if not foto_elegida: # Si no se cambia la foto, dejamos la que está
            foto_elegida = anuncio_a_editar.foto
        else: # Si se cambia, la cambiamos y borramos la anterior del directorio físico de MEDIA/FOTOGRAFIAS
            foto_elegida = request.FILES.get("foto")
            if anuncio_a_editar.foto:
                os.remove(settings.BASE_DIR + anuncio_a_editar.foto.url)


        anuncio = models.Anuncio(id= id_anuncio_elegido, fecha=fecha_hoy, tipo=tipo_elegido, categoria=categoria_elegida, titulo=titulo_elegido,
                                 descripcion=descripcion_elegida, precio=precio_elegido, nomyapell=nomyapell_elegidos,
                                 foto=foto_elegida, usuario=usuario_actual)
        anuncio.save()

        return redirect("guardar-cambios-anuncio/edicion-ok")
    else:  # algo no ha ido bien. Se han saltado la seguridad HTML.
        return render(request, "registro-ko.html")

def edicion_ok(request):
    return render(request, "edicion-ok.html")

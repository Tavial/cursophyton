from flask import Flask, render_template,session, jsonify
from flask.globals import request
from clases import modelo
from operaciones_bd import operaciones_bd_anuncios, operaciones_bd_escalas, operaciones_bd_tipos, operaciones_bd_mensajes
from flask_mail import Mail, Message #imports necesarios para el envío de correos al usuario
import string
import random
import os



app = Flask (__name__)

app.config["UPLOAD_FOLDER"] = os.path.abspath("./static/imagenes/")
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024 # 0.5 MB tamaño máximo

app.config["MAIL_SERVER"] = "smtp.gmail.com"  #configura el servidor para el envío de emails
app.config["MAIL_PORT"] = 587 # tiene que ser obligatoriamente por este puerto porque si no no funciona
app.config["MAIL_USE_TLS"] = True # parámetro de seguridad que tiene que estar a True
app.config["MAIL_USERNAME"] = "tavial.flask@gmail.com" # cuenta de gmail que vamos a utilizar para el envío de mensajes
app.config["MAIL_PASSWORD"] = "frwyapvmoepuiipv" # password generado en la cuenta de gmail tras activar la identificación en dos pasos.
mail = Mail(app) # cuando queramos enviar un email lo haremos a través de este objeto mail

#Vamos a usar la sesión para el cliente administrador
app.secret_key = "Ferrosale"


@app.route ("/admin/",methods=["GET","POST"])
def administracion_inicio():
    return render_template ("admin/admin-login.html", error_login="")


@app.route ("/admin/<string:ruta>",methods=["GET","POST"]) #cualquier ruta que se ponga después de admin va a ejecutarse en esta función
#si queremos hacer comprobaciones de seguridad, lo hacemos desde un mismo sitio
#si no ponemos nada dará un error por lo que también lo tenemos que contemplar en @app.route ("/admin/")
def administracion(ruta):
    # aquí vamos gestionando todas las alternativas a admin/XXXX
    if ruta == "login-admin": #cogemos los valores del formulario de identificacion

        clave_introducida = request.form.get ("clave")

        if clave_introducida == "Tatiana":
            # metemos el sello al usuario administrador
            session ["identificado"] = "id_administrador"

            lista_anuncios = operaciones_bd_anuncios.listar_anuncios()
            lista_escalas = operaciones_bd_escalas.obtener_escalas()
            lista_tipos = operaciones_bd_tipos.obtener_tipos()
            escala = request.form.get("escala")
            tipo = request.form.get("tipo")

            # No se ha seleccionado nada todavía
            if escala == None:
                escala = "Todos"
            if tipo == None:
                tipo = "Todos"

            return render_template("admin/admin-index.html", var_lista_anuncios=lista_anuncios,var_lista_escalas=lista_escalas, var_lista_tipos=lista_tipos, var_escala=escala, var_tipo=tipo)
        else:
            return render_template ("admin/admin-login.html",error_login="Password incorrecta")

    if not "identificado" in session:
        return render_template("admin/admin-restringido.html")

    if ruta == "admin-borrar-anuncio":
        #tengo que coger el id que nos llega de la ruta admin-borrar-anuncio y que me indica el anuncio a borrar
        id = request.args.get("id")
        escala = request.form.get("escala")
        tipo = request.form.get("tipo")

        # No se ha seleccionado nada todavía
        if escala == None:
            escala = "Todos"
        if tipo == None:
            tipo = "Todos"

        operaciones_bd_anuncios.borrar_anuncio(id)
        lista_anuncios = operaciones_bd_anuncios.listar_anuncios()

        lista_escalas = operaciones_bd_escalas.obtener_escalas()
        lista_tipos = operaciones_bd_tipos.obtener_tipos()
        return render_template("admin/admin-index.html", var_lista_anuncios=lista_anuncios, var_escala=escala, var_tipo=tipo, var_lista_escalas = lista_escalas, var_lista_tipos = lista_tipos)

    if ruta == "admin-editar-anuncio":
        #cuando escogemos editar anuncio, recogemos el id que nos llega de la ruta admin-editar-anuncio
        id = request.args.get ("id")

        #con este id consultamos la base datos para obtener el resto de los campos
        anuncio = operaciones_bd_anuncios.obtener_anuncio(id)

        return render_template("admin/admin-editar-anuncio.html",var_anuncio=anuncio)
    if ruta == "modificar-anuncio":
        anuncio_a_modificar = modelo.Anuncio ()
        anuncio_a_modificar.id = request.form.get("id")
        anuncio_a_modificar.escala = request.form.get("escala")
        anuncio_a_modificar.tipo = request.form.get("tipo")
        anuncio_a_modificar.titulo = request.form.get("titulo")
        anuncio_a_modificar.descripcion = request.form.get("descripcion")
        anuncio_a_modificar.precio = request.form.get("precio")
        anuncio_a_modificar.nomyapell = request.form.get("nombre")
        anuncio_a_modificar.email = request.form.get("email")
        anuncio_a_modificar.emailOK = request.form.get("emailOK")
        foto = request.files["imagen"]
        anuncio_a_modificar.foto = foto.filename

        escala = request.form.get("escala")
        tipo = request.form.get("tipo")

        # No se ha seleccionado nada todavía
        if escala == None:
            escala = "Todos"
        if tipo == None:
            tipo = "Todos"

        # guardamos la imagen en el directorio imagenes
        archivo = str(anuncio_a_modificar.foto)
        if archivo != "":  # el usuario carga una imagen
            archivo = archivo.split('.')
            nombre = str(anuncio_a_modificar.id)
            extension = archivo[1]
            nombre_archivo = nombre + "." + extension
            foto.save(os.path.join(app.config["UPLOAD_FOLDER"], nombre_archivo))
            # modificamos este campo en la base de datos
            print (str(anuncio_a_modificar.id)+str(anuncio_a_modificar.titulo))
            operaciones_bd_anuncios.modificar_anuncio(anuncio_a_modificar)
            operaciones_bd_anuncios.modificar_nombre_imagen(anuncio_a_modificar.id, nombre_archivo)
        else: # si el usuario no carga nada, se queda como está en la base de datos
            operaciones_bd_anuncios.modificar_anuncio_sin_imagen(anuncio_a_modificar)

        lista_anuncios = operaciones_bd_anuncios.listar_anuncios()
        aleatorio = random.randint(1,5000000)
        lista_escalas = operaciones_bd_escalas.obtener_escalas()
        lista_tipos = operaciones_bd_tipos.obtener_tipos()
        return render_template("admin/admin-index.html", var_lista_anuncios=lista_anuncios,cache_breaker=aleatorio,var_escala=escala, var_tipo=tipo, var_lista_escalas = lista_escalas, var_lista_tipos = lista_tipos)

    if ruta == "admin-listados":
        lista_escalas = operaciones_bd_escalas.obtener_escalas()
        lista_tipos = operaciones_bd_tipos.obtener_tipos()
        # Recogemos los valores del formulario de escala y tipo seleccionados.
        escala = request.form.get("escala")
        tipo = request.form.get("tipo")

        if bool(request.form.get("check_no_validado")):
            validado = "NO"
        else:
            validado = "SI"

        if escala =="Todos":
            if (tipo =="Todos" and validado =="NO") or (tipo =="Todos" and validado=="SI"):
                #Tenemos que hacer un listado que nos saque TODOS los anuncios validados y no validados
                lista_anuncios =operaciones_bd_anuncios.listado_todos_emailOK(validado)
            elif (tipo != "Todos" and validado == "NO") or (tipo != "Todos" and validado == "SI"):
                #Tenemos que hacer un listado que nos saque todas las escalas de un tipo determinado validados y no validados
                lista_anuncios = operaciones_bd_anuncios.listado_tipo_emailOK(tipo,validado)
        else:
            if (tipo =="Todos" and validado =="NO") or (tipo == "Todos" and validado =="SI"):
                #Tenemos que hacer un listado que nos saque los anuncios de una escala determinada de cualquier tipo validados y no validados
                lista_anuncios = operaciones_bd_anuncios.listado_escala_emailOK(escala, validado)
            elif (tipo != "Todos" and validado == "NO") or (tipo != "Todos" and validado == "SI"):
                #Tenemos que hacer un listado que nos saque los anuncios de una escala y un tipo determinado validados y no validados
                lista_anuncios = operaciones_bd_anuncios.listado_escala_tipo_emailOK(escala, tipo, validado)
        aleatorio = random.randint(1, 5000000)
        return render_template("admin/admin-listados.html", var_lista_anuncios=lista_anuncios, cache_breaker=aleatorio, var_lista_escalas=lista_escalas,var_lista_tipos=lista_tipos, var_escala=escala, var_tipo=tipo)

    if ruta == "cerrar-sesion":
        session.clear()
        return render_template ("admin/admin-fin-sesion.html")


@app.route("/")
def index ():
    lista_anuncios= operaciones_bd_anuncios.listar_anuncios_validados()
    lista_escalas = operaciones_bd_escalas.obtener_escalas()
    lista_tipos = operaciones_bd_tipos.obtener_tipos()

    escala = request.args.get("escala")
    tipo = request.args.get("tipo")

    # No se ha seleccionado nada todavía
    if escala==None:
        escala="Todos"
    if tipo==None:
        tipo="Todos"

    numero_anuncios = len(lista_anuncios)
    paginacion = 3

    numero_paginas = int(numero_anuncios // paginacion)

    if (numero_anuncios % paginacion) != 0:
        numero_paginas += 1


    pagina_solicitada = str(request.args.get("pagina"))

    if pagina_solicitada.isnumeric():
        if int(pagina_solicitada) >= 0 and int(pagina_solicitada) < numero_paginas:
            pagina_actual = int(pagina_solicitada)
        else:
            pagina_actual = 0
    else:
        pagina_actual = 0

    limite_inferior = pagina_actual * paginacion
    limite_superior = limite_inferior + paginacion
    if limite_superior > numero_anuncios:
        limite_superior = numero_anuncios

    lista_anuncios_reducida = []

    for ia in range (limite_inferior,limite_superior):
        lista_anuncios_reducida.append (lista_anuncios[ia])

    if pagina_actual > 0 and pagina_actual <= numero_paginas:
        pagina_anterior = pagina_actual-1
    else:
        pagina_anterior = 0

    if pagina_actual >=0 and pagina_actual < numero_paginas-1:
        pagina_siguiente = pagina_actual+1
    else:
        pagina_siguiente = pagina_actual

    if numero_paginas != 0:
        texto_paginacion = str(pagina_actual + 1) + " de " + str(numero_paginas)
    else:
        texto_paginacion = "No existen anuncios"

    return render_template("index.html", var_lista_anuncios=lista_anuncios_reducida, var_lista_escalas=lista_escalas, var_lista_tipos=lista_tipos,var_pagina_anterior=pagina_anterior, var_pagina_siguiente=pagina_siguiente,var_texto_paginacion=texto_paginacion, var_escala=escala, var_tipo=tipo)



@app.route ("/listados",methods= ["POST"])
def definir_listados ():
    lista_escalas = operaciones_bd_escalas.obtener_escalas()
    lista_tipos = operaciones_bd_tipos.obtener_tipos()
    validado = "SI"
    lista_anuncios = operaciones_bd_anuncios.listado_todos_emailOK(validado)

    # Recogemos los valores del formulario de escala y tipo seleccionados.
    escala = request.form.get ("escala")
    tipo = request.form.get ("tipo")

    # No se ha seleccionado nada todavía
    if escala == None:
        escala = "Todos"
    if tipo == None:
        tipo = "Todos"

    numero_anuncios = len(lista_anuncios)
    paginacion = 3

    numero_paginas = int(numero_anuncios // paginacion)

    if (numero_anuncios % paginacion) != 0:
        numero_paginas += 1

    pagina_solicitada = str(request.args.get("pagina"))

    if pagina_solicitada.isnumeric():
        if int(pagina_solicitada) >= 0 and int(pagina_solicitada) < numero_paginas:
            pagina_actual = int(pagina_solicitada)
        else:
            pagina_actual = 0
    else:
        pagina_actual = 0

    limite_inferior = pagina_actual * paginacion
    limite_superior = limite_inferior + paginacion
    if limite_superior > numero_anuncios:
        limite_superior = numero_anuncios

    lista_anuncios_reducida = []

    for ia in range(limite_inferior, limite_superior):
        lista_anuncios_reducida.append(lista_anuncios[ia])

    if pagina_actual > 0 and pagina_actual <= numero_paginas:
        pagina_anterior = pagina_actual - 1
    else:
        pagina_anterior = 0

    if pagina_actual >= 0 and pagina_actual < numero_paginas - 1:
        pagina_siguiente = pagina_actual + 1
    else:
        pagina_siguiente = pagina_actual

    if numero_paginas != 0:
        texto_paginacion = str(pagina_actual + 1) + " de " + str(numero_paginas)
    else:
        texto_paginacion = "No existen anuncios"

    if escala == "Todos":
        if tipo == "Todos":
            # Tenemos que hacer un listado que nos saque TODOS los anuncios validados
            return render_template("index.html", var_lista_anuncios=lista_anuncios_reducida, var_pagina_anterior=pagina_anterior, var_pagina_siguiente=pagina_siguiente,var_texto_paginacion=texto_paginacion,var_lista_escalas=lista_escalas, var_lista_tipos=lista_tipos, var_escala=escala, var_tipo=tipo)
        elif tipo != "Todos":
            # Tenemos que hacer un listado que nos saque los anuncios validados de todas las escalas de un tipo determinado
            lista_anuncios = operaciones_bd_anuncios.listado_tipo_emailOK(tipo, validado)
            return render_template("listados.html", var_lista_anuncios=lista_anuncios, var_lista_escalas=lista_escalas,var_lista_tipos=lista_tipos, var_escala=escala, var_tipo=tipo)
    else:
        if tipo == "Todos":
            # Tenemos que hacer un listado que nos saque los anuncios validados de una escala determinada de cualquier tipo
            lista_anuncios = operaciones_bd_anuncios.listado_escala_emailOK(escala, validado)
            return render_template("listados.html", var_lista_anuncios=lista_anuncios, var_lista_escalas=lista_escalas,var_lista_tipos=lista_tipos, var_escala=escala, var_tipo=tipo)
        elif tipo != "Todos":
            # Tenemos que hacer un listado que nos saque los anuncios validados de una escala y un tipo determinado
            lista_anuncios = operaciones_bd_anuncios.listado_escala_tipo_emailOK(escala, tipo, validado)
            return render_template("listados.html", var_lista_anuncios=lista_anuncios, var_lista_escalas=lista_escalas,var_lista_tipos=lista_tipos, var_escala=escala, var_tipo=tipo)


@app.route("/publicar-anuncio")
def publicar_anuncio():
    lista_escalas = operaciones_bd_escalas.obtener_escalas()
    lista_tipos = operaciones_bd_tipos.obtener_tipos ()
    return render_template("formulario-publicar-anuncio.html",var_lista_escalas=lista_escalas, var_lista_tipos=lista_tipos)

@app.route("/guardar-anuncio",methods= ["POST"])#va a ser el action del formulario.
def guardar_anuncio():
    #calculamos la fecha actual
    fechaActual = modelo.Fecha()
    fecha = fechaActual.mostrarFecha()
    #recogemos los valores de los componentes del formulario en unas variables.
    escala = request.form.get("escala")
    tipo = request.form.get("tipo")
    titulo = request.form.get("titulo")
    descripcion = request.form.get("descripcion")
    precio = request.form.get("precio")
    nomyapell = request.form.get("nombre")
    email = request.form.get("email")
    foto = request.files["imagen"]
    imagen = foto.filename

    # Hacemos la doble validación tras la del formulario HtML por código para los campos
    validador = modelo.Validador()
    titulo_valido = validador.noVacio(str(titulo))
    precio_valido = validador.numReal(str(precio))
    nomyapell_validos = validador.nombreApellidos(str(nomyapell))
    email_valido = validador.email(str(email))
    if titulo_valido and precio_valido and nomyapell_validos and email_valido:
        # voy a generar un código de comprobación para validar el anuncio
        # importo random y string
        letras = string.ascii_letters +"0123456789"
        codigo_aleatorio = "".join(random.choices(letras, k=60))

        nuevo_anuncio = modelo.Anuncio(fecha, escala, tipo, titulo, descripcion, precio, nomyapell, email,"NO",codigo_aleatorio,imagen)

        id_generado = operaciones_bd_anuncios.publicar_anuncio(nuevo_anuncio) # Además de registrar el anuncio nos devuelve el id generado.

        # guardamos la imagen en el directorio imagenes
        archivo = str(imagen)
        if archivo != "":  # el usuario carga una imagen
            archivo = archivo.split('.')
            nombre = str(id_generado)
            extension = archivo[1]
            nombre_archivo = nombre + "." + extension
            foto.save(os.path.join(app.config["UPLOAD_FOLDER"], nombre_archivo))
        else:  # el usuario no carga imagen
            nombre_archivo = "sin_imagen.png"

        #modificamos este campo en la base de datos
        operaciones_bd_anuncios.modificar_nombre_imagen(id_generado,nombre_archivo)


        #enviamos email al usuario agradeciéndole la publicación del anuncio.
        #primero ponemos el asunto y luego indicamos el nombre del email origen (el nuestro) y luego ponemos los destinatarios.
        mensaje_email = Message("FerroSale. Modelismo ferroviario",
                                sender= "tavial.flask@gmail.com",
                                recipients = [email])
        #Ahora vamos a redactar el cuerpo del correo
        # así mandamos texto plano en el email
        # mensaje_email.body = str(nomyapell)+" te agradecemos que hayas registrado tu anuncio en nuestro portal Ferrosale"

        #podemos llamar a una página web o bien escribir nosotros directamente el mensaje.

        #la interrogación es para pasarle información adicional. Ahi le vamos a pasar el id
        mensaje_email.html = str(nomyapell)+", muchas gracias por utilizar nuestro servicio. <br/>  <a href='http://192.168.100.105:5000/validar-anuncio?id={}&codigo={}'> Pincha en este enlace para validar tu anuncio </a>".format(str(id_generado),str(codigo_aleatorio))

        mail.send(mensaje_email)

        return render_template("publicacion-ok.html")

    else:
        return render_template("pagina-error.html")


########  ruta para validar el anuncio por email  ############

@app.route("/validar-anuncio")
def validar_anuncio():

    """
    Cuando registramos cada anuncio se le va a asignar un id único que se lo pasamos embebido en la cabecera de la url
    al usuario en la variable id. En el momento que el usuario pulsa ese enlace de validar nos manda la url de la cual
    tenemos que sacar el valor id que identifica al anuncio que él ha publicado, Este dato lo recogemos con
    request.args.get("id") siendo el valor de id el identificador del anuncio que se va a validar

    El programa espera o otro alta o una validación. Pero puede tener 5 altas seguidas y 1ó 2 validaciones.
    """

    id = request.args.get("id")
    codigo = request.args.get("codigo")

    resultado = operaciones_bd_anuncios.verificar_codigo_anuncio(id,codigo)
    if resultado == 0:
        return render_template("anuncio-NO-validado.html",valor_id=str(id))


    if resultado == 1:
        fechaActual = modelo.Fecha()
        fecha = fechaActual.mostrarFecha()
        operaciones_bd_anuncios.validar_email_anuncio(id,fecha)
        return render_template("anuncio-validado.html")

@app.route ("/dejar-comentario")
def dejar_comentario():
    return render_template ("dejar-comentario.html")

# comienzo del servicio REST
@app.route("/registrar-mensaje",methods=["GET","POST"])
def registrar_mensaje():
    nombre = request.args.get("n")
    mensaje = request.args.get("m")
    operaciones_bd_mensajes.registrar_mensaje(nombre,mensaje)
    return "ok"

@app.route("/obtener-mensajes")
def obtener_mensajes():
    mensajes = operaciones_bd_mensajes.obtener_mensajes()
    return jsonify (mensajes)

app.run (debug=True, host="192.168.100.105", port=5000)

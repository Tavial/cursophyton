import mysql.connector
from operaciones_bd.constantes_sql import SQL_PUBLICAR_ANUNCIO, SQL_LISTAR_ANUNCIOS, SQL_VALIDAR_ANUNCIO, SQL_VERIFICAR_CODIGO_ANUNCIO
from operaciones_bd.constantes_sql import SQL_MODIFICAR_ARCHIVO, SQL_BORRAR_ANUNCIO, SQL_OBTENER_ANUNCIO
from operaciones_bd.constantes_sql import SQL_MODIFICAR_ANUNCIO, SQL_MODIFICAR_SIN_IMAGEN, SQL_LISTADO_ESCALA_TIPO
from operaciones_bd.constantes_sql import SQL_LISTADO_TODOS_EMAILOK, SQL_LISTADO_TIPO_EMAILOK, SQL_LISTADO_ESCALA_EMAILOK
from operaciones_bd.constantes_sql import SQL_LISTADO_ESCALA_TIPO_EMAILOK, SQL_LISTAR_ANUNCIOS_VALIDADOS

def conectar ():
    mydb = mysql.connector.connect (
        host = "localhost",
        user = "root",
        database = "bd_ferrosale"
    )
    return mydb

def publicar_anuncio (nuevo_anuncio):
    sql = SQL_PUBLICAR_ANUNCIO
    mydb = conectar()
    try:
        cursor = mydb.cursor()
        tupla = (nuevo_anuncio.fecha, nuevo_anuncio.escala, nuevo_anuncio.tipo, nuevo_anuncio.titulo, nuevo_anuncio.descripcion, nuevo_anuncio.precio, nuevo_anuncio.nomyapell, nuevo_anuncio.email, nuevo_anuncio.codigo, nuevo_anuncio.foto)
        cursor.execute (sql,tupla)
        mydb.commit()
        id_generado = cursor.lastrowid # con esto obtenemos el último id generado ya que lo vamos a necesitar para asociarlo con código de validación que le vamos a enviar al usuario.
    except Exception as e:
        print (e)
    finally:
        if mydb is not None:
            mydb.disconnect()
    return id_generado

def modificar_anuncio (anuncio):
    sql = SQL_MODIFICAR_ANUNCIO
    mydb = conectar()
    try:
        cursor = mydb.cursor()
        tupla = (anuncio.escala, anuncio.tipo, anuncio.titulo, anuncio.descripcion, anuncio.precio, anuncio.nomyapell, anuncio.email, anuncio.emailOK, anuncio.foto, anuncio.id)
        cursor.execute (sql,tupla)
        mydb.commit()
    except Exception as e:
        print (e)
    finally:
        if mydb is not None:
            mydb.disconnect()

def modificar_anuncio_sin_imagen (anuncio):
    sql = SQL_MODIFICAR_SIN_IMAGEN
    mydb = conectar()
    try:
        cursor = mydb.cursor()
        tupla = (anuncio.escala, anuncio.tipo, anuncio.titulo, anuncio.descripcion, anuncio.precio, anuncio.nomyapell, anuncio.email, anuncio.emailOK, anuncio.id)
        cursor.execute (sql,tupla)
        mydb.commit()
    except Exception as e:
        print (e)
    finally:
        if mydb is not None:
            mydb.disconnect()

def listar_anuncios():
    sql = SQL_LISTAR_ANUNCIOS
    mydb = conectar()
    listado_anuncios = None
    try:
        cursor = mydb.cursor()
        cursor.execute(sql)
        listado_anuncios = cursor.fetchall()
    except Exception as e:
        print (e)
    finally:
        if mydb is not None:
            mydb.disconnect()
    return listado_anuncios

def listar_anuncios_validados():
    sql = SQL_LISTAR_ANUNCIOS_VALIDADOS
    mydb = conectar()
    listado_anuncios = None
    try:
        cursor = mydb.cursor()
        cursor.execute(sql)
        listado_anuncios = cursor.fetchall()
    except Exception as e:
        print(e)
    finally:
        if mydb is not None:
            mydb.disconnect()
    return listado_anuncios

def verificar_codigo_anuncio (id,codigo):
    sql = SQL_VERIFICAR_CODIGO_ANUNCIO
    mydb = conectar()
    listado_anuncios = None
    try:
        cursor = mydb.cursor()
        tupla = (id,codigo)
        cursor.execute(sql,tupla)
        listado_anuncios = cursor.fetchall() # devuelve una lista con los elementos que tienen el id y el código que les
        # indicamos. Esta lista tendrá una longitud de 1 si lo encuentra o 0 si no encuentra esa coincidencia
    except Exception as e:
        print (e)
    finally:
        if mydb is not None:
            mydb.disconnect ()
    return len(listado_anuncios) # si es 0 es que el id y el código no son válidos (el usuario pudo modificar en la url
                                 # que se le pasó para verificar alguno de los valores a mano por tanto al devolvérnoslo
                                 # en nuestra base de datos no vamos a tener esa coincidencia). Un 1 es que encuentra el
                                 # elemento que coincide.

def validar_email_anuncio (id,fecha):
    sql = SQL_VALIDAR_ANUNCIO
    mydb = conectar ()
    try:
        cursor = mydb.cursor()
        tupla = (fecha,id)
        cursor.execute (sql,tupla)
        mydb.commit()
    except Exception as e:
        print (e)
    finally:
        if mydb is not None:
            mydb.disconnect()

def modificar_nombre_imagen (id,nom_imagen):
    sql = SQL_MODIFICAR_ARCHIVO
    mydb = conectar()
    try:
        cursor = mydb.cursor()
        tupla = (nom_imagen,id)
        cursor.execute(sql, tupla)
        mydb.commit()
    except Exception as e:
        print(e)
    finally:
        if mydb is not None:
            mydb.disconnect()


def borrar_anuncio (id):
    sql = SQL_BORRAR_ANUNCIO
    mydb = conectar()
    try:
        cursor = mydb.cursor()
        tupla = (id,)
        cursor.execute (sql,tupla)
        mydb.commit()
    except Exception as e:
        print (e)
    finally:
        if mydb is not None:
            mydb.disconnect()

def obtener_anuncio (id):
    sql = SQL_OBTENER_ANUNCIO
    mydb = conectar()
    try:
        cursor = mydb.cursor()
        tupla = (id,)
        cursor.execute (sql,tupla)
        anuncio_obtenido = cursor.fetchone()
    except Exception as e:
        print (e)
    finally:
        if mydb is not None:
            mydb.disconnect()
    return anuncio_obtenido

def listado_escala_tipo (escala,tipo):
    sql = SQL_LISTADO_ESCALA_TIPO
    mydb = conectar()
    listaxescalaxtipo = None
    try:
        cursor = mydb.cursor()
        tupla = (escala,tipo)
        cursor.execute(sql,tupla)
        listaxescalaxtipo = cursor.fetchall()
    except Exception as e:
        print(e)
    finally:
        if mydb is not None:
            mydb.disconnect()
    return listaxescalaxtipo

def listado_todos_emailOK (emailOK):
    sql = SQL_LISTADO_TODOS_EMAILOK
    mydb = conectar()
    lista = None
    try:
        cursor = mydb.cursor()
        tupla = (emailOK,)
        cursor.execute(sql,tupla)
        lista = cursor.fetchall()
    except Exception as e:
        print(e)
    finally:
        if mydb is not None:
            mydb.disconnect()
    return lista

def listado_tipo_emailOK(tipo,emailOK):
    sql = SQL_LISTADO_TIPO_EMAILOK
    mydb = conectar()
    lista = None
    try:
        cursor = mydb.cursor()
        tupla = (tipo, emailOK)
        cursor.execute(sql, tupla)
        lista = cursor.fetchall()
    except Exception as e:
        print(e)
    finally:
        if mydb is not None:
            mydb.disconnect()
    return lista

def listado_escala_emailOK(escala, emailOK):
    sql = SQL_LISTADO_ESCALA_EMAILOK
    mydb = conectar()
    lista = None
    try:
        cursor = mydb.cursor()
        tupla = (escala, emailOK)
        cursor.execute(sql, tupla)
        lista = cursor.fetchall()
    except Exception as e:
        print(e)
    finally:
        if mydb is not None:
            mydb.disconnect()
    return lista

def listado_escala_tipo_emailOK(escala, tipo, emailOK):
    sql = SQL_LISTADO_ESCALA_TIPO_EMAILOK
    mydb = conectar()
    lista = None
    try:
        cursor = mydb.cursor()
        tupla = (escala, tipo, emailOK)
        cursor.execute(sql, tupla)
        lista = cursor.fetchall()
    except Exception as e:
        print(e)
    finally:
        if mydb is not None:
            mydb.disconnect()
    return lista
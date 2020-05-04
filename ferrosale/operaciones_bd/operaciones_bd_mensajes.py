import mysql.connector
from operaciones_bd.constantes_sql import SQL_INSERTAR_MENSAJE, SQL_OBTENER_MENSAJES

def conectar ():
    mydb = mysql.connector.connect (
        host = "localhost",
        user = "root",
        database = "bd_ferrosale"
    )
    return mydb

def registrar_mensaje (nombre, mensaje):
    sql = SQL_INSERTAR_MENSAJE
    mydb = conectar()
    try:
        cursor = mydb.cursor()
        tupla = (nombre, mensaje)
        cursor.execute (sql, tupla)
        mydb.commit()
    except Exception as e:
        print (e)
    finally:
        if mydb is not None:
            mydb.disconnect()

def obtener_mensajes ():
    sql = SQL_OBTENER_MENSAJES
    mydb = conectar()
    lista_mensajes = None
    try:
        cursor = mydb.cursor()
        cursor.execute (sql)
        lista_mensajes = cursor.fetchall()
    except Exception as e:
        print (e)
    finally:
        if mydb is not None:
            mydb.disconnect()
    return lista_mensajes
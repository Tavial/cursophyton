import mysql.connector
from operaciones_bd.constantes_sql import SQL_OBTENER_TIPOS

def conectar ():
    mydb = mysql.connector.connect (
        host = "localhost",
        user = "root",
        database = "bd_ferrosale"
    )
    return mydb

def obtener_tipos ():
    sql = SQL_OBTENER_TIPOS
    mydb = conectar()
    tipos = None
    try:
        cursor = mydb.cursor()
        cursor.execute (sql)
        tipos = cursor.fetchall()
    except Exception as e:
        print (e)
    finally:
        if mydb is not None:
            mydb.disconnect()
    return tipos
import mysql.connector
from operaciones_bd.constantes_sql import SQL_OBTENER_ESCALAS

def conectar ():
    mydb = mysql.connector.connect (
        host = "localhost",
        user = "root",
        database = "bd_ferrosale"
    )
    return mydb

def obtener_escalas ():
    sql = SQL_OBTENER_ESCALAS
    mydb = conectar()
    escalas = None
    try:
        cursor = mydb.cursor()
        cursor.execute (sql)
        escalas = cursor.fetchall()
    except Exception as e:
        print (e)
    finally:
        if mydb is not None:
            mydb.disconnect()
    return escalas
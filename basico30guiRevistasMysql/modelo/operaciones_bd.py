import mysql.connector
from modelo import constantes_sql, clases

def conectar():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        database ="bd_revistas"
    )
    return mydb

#método que recibe un onjeto de la clase Revista
#para registrarla en la base de datos

def registro_revista(revista):
    sql = constantes_sql.SQL_INSERCION_REVISTA
    mydb = conectar()
    cursor = mydb.cursor()
    # mirando el orden de insert de la sql formo la siguiente 
    # tupla com los valores a insertar en base de datos 
    val = (revista.titulo,revista.precio, revista.tema)
    # lanzamos la sql aplicándole la tupla. Así no permite introducir ningún valor que nosotros no hayamos puesto
    # hace la traducción de %s y %f. Se hace por seguridad
    cursor.execute (sql,val) 
    mydb.commit()
    mydb.disconnect()

def obtener_revistas():
    sql =constantes_sql.SQL_LISTADO_REVISTAS
    mydb = conectar ()
    cursor = mydb.cursor ()
    cursor.execute (sql) # lanza la consulta sql
    resultado_lista = cursor.fetchall() # devuelve el resultado de la SELECT sobre la base de datos en forma de array o lista
    mydb.disconnect()
    return resultado_lista

def borrar_revista (revista_id):
    sql = constantes_sql.SQL_BORRADO_REVISTA
    mydb = conectar ()
    cursor = mydb.cursor()
    val = (revista_id,)
    cursor.execute (sql,val)
    mydb.commit()
    mydb.disconnect()
    
def obtener_revista(revista_id):
    sql = constantes_sql.SQL_OBTENER_REVISTA
    mydb = conectar ()
    cursor = mydb.cursor()
    val = (revista_id,)
    cursor.execute (sql,val)
    resultado_lista = cursor.fetchone() #Devuelve el resultado de la SELECT sin corchetes. Es para un resultado
    # Metemos el resultado de la lista en un objeto para mostrarlo en pantalla.
    revista_a_editar = clases.Revista (id = resultado_lista [0], titulo = resultado_lista[1] ,precio = resultado_lista[2], tema = resultado_lista[3])
    mydb.disconnect()
    
    return revista_a_editar

def modificar_revista (revista):
    sql = constantes_sql.SQL_MODIFICAR_REVISTA
    mydb = conectar()
    cursor = mydb.cursor()
    val = (revista.titulo,revista.precio, revista.tema, revista.id)
    cursor.execute (sql,val)
    mydb.commit()
    mydb.disconnect()
    
    
    
    
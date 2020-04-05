import mysql.connector
from modelo import constantes_sql



def conectar ():
    mydb = mysql.connector.connect(
        
        host = "localhost",
        user = "root",
        database = "bd_model_ferro"    
         
        )
    return mydb

def registro_producto (producto):
    sql = constantes_sql.SQL_INSERCION_PRODUCTO
    # conectamos a la base de datos.
    mydb = conectar ()
    cursor = mydb.cursor ()
    tupla = (producto.referencia, producto.nombre, producto.tipo, producto.escala, producto.fabricante, producto.precio, producto.stock, producto.descripcion,producto.imagen )
    #lanzamos la SQL con la tupla
    cursor.execute (sql,tupla)
    #pedimos que se ejecute la transacción en la base de datos
    mydb.commit ()
    #desconectamos la base de datos.
    mydb.disconnect()
    
def listar_productos():
    sql = constantes_sql.SQL_LISTADO_PRODUCTOS
    # conectamos a la base de datos
    mydb = conectar ()
    cursor = mydb.cursor()
    #lanzamos la SQL
    cursor.execute (sql)
    resultado_lista = cursor.fetchall() # devuelve el resultado de la SELECT sobre la base de datos en forma de array o lista
    #desconectamos la base de datos.
    mydb.disconnect()
    return resultado_lista
    
    

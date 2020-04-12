import mysql.connector
from modelo import constantes_sql, clases



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

def borrar_producto(referencia):
    sql = constantes_sql.SQL_BORRRAR_PRODUCTO
    mydb = conectar ()
    cursor = mydb.cursor()
    tupla = (referencia,) #ponemos la coma porque si no no lo considera tupla.
    cursor.execute (sql,tupla)  
    mydb.commit()
    mydb.disconnect() 
    
def obtener_producto(referencia):   
    sql = constantes_sql.SQL_OBTENER_PRODUCTO_POR_REF
    mydb = conectar ()
    cursor = mydb.cursor()
    tupla = (referencia,)
    cursor.execute (sql,tupla)
    producto_obtenido = cursor.fetchone()
    mydb.disconnect()
    elemento = clases.Producto(referencia = producto_obtenido[0], nombre = producto_obtenido[1], \
        tipo = producto_obtenido[2], escala = producto_obtenido[3], fabricante = producto_obtenido[4], \
        precio = producto_obtenido[5], stock = producto_obtenido[6], descripcion = producto_obtenido[7], \
        imagen = producto_obtenido[8])
    return elemento
    
def guardar_cambios_producto (producto): 
    sql = constantes_sql.SQL_GUARDAR_CAMBIOS_PRODUCTO
    mydb = conectar ()
    cursor = mydb.cursor()
    tupla = (producto.nombre, producto.tipo, producto.escala, producto.fabricante, producto.precio, producto.stock, producto.descripcion,producto.imagen, producto.referencia)
    cursor.execute (sql,tupla)
    mydb.commit()
    mydb.disconnect()

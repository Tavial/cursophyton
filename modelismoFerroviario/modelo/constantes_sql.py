SQL_INSERCION_PRODUCTO ="INSERT INTO `tabla_productos` (`referencia`, `nombre`, `tipo`, `escala`, `fabricante`, `precio`, `stock`, `descripcion`, `imagen`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"

SQL_LISTADO_PRODUCTOS = "SELECT * FROM tabla_productos ;"

SQL_BORRRAR_PRODUCTO = "DELETE FROM tabla_productos WHERE referencia = %s ;"

SQL_OBTENER_PRODUCTO_POR_REF = "SELECT * FROM tabla_productos WHERE referencia = %s ;"

SQL_GUARDAR_CAMBIOS_PRODUCTO = "UPDATE tabla_productos SET nombre = %s, tipo = %s, escala = %s, fabricante = %s, precio = %s, stock = %s, descripcion = %s, imagen = %s WHERE referencia = %s ;"

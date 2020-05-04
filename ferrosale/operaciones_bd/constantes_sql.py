"""
SQL para manejo de la base de datos bd_ferrosale

"""
SQL_OBTENER_ESCALAS ="SELECT * FROM tabla_escalas;"
SQL_OBTENER_TIPOS = "SELECT * FROM tabla_tipos;"

SQL_LISTAR_ANUNCIOS = "SELECT ta.id, ta.fecha, te.escala, tt.tipo, ta.titulo, ta.descripcion, ta.precio, ta.nomyapell, ta.email, ta.emailOK, ta.foto FROM tabla_anuncios_venta as ta, tabla_escalas as te, tabla_tipos as tt WHERE ta.id_escala = te.id AND ta.id_tipo = tt.id ORDER BY ta.id DESC;"
SQL_LISTAR_ANUNCIOS_VALIDADOS = "SELECT ta.id, ta.fecha, te.escala, tt.tipo, ta.titulo, ta.descripcion, ta.precio, ta.nomyapell, ta.email, ta.emailOK, ta.foto FROM tabla_anuncios_venta as ta, tabla_escalas as te, tabla_tipos as tt WHERE ta.id_escala = te.id AND ta.id_tipo = tt.id AND ta.emailOK='SI' ORDER BY ta.id DESC;"

SQL_PUBLICAR_ANUNCIO = "INSERT INTO `tabla_anuncios_venta` (`id`, `fecha`, `id_escala`, `id_tipo`, `titulo`, `descripcion`, `precio`, `nomyapell`, `email`, `emailOK`, `codigo`, `foto`) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s, 'NO', %s, %s);"

SQL_VERIFICAR_CODIGO_ANUNCIO = "SELECT titulo FROM tabla_anuncios_venta WHERE id= %s AND codigo= %s; "

SQL_VALIDAR_ANUNCIO = "UPDATE tabla_anuncios_venta SET emailOK = 'SI', fecha = %s WHERE id = %s;"
SQL_MODIFICAR_ARCHIVO = "UPDATE tabla_anuncios_venta SET foto = %s WHERE id = %s; "


SQL_BORRAR_ANUNCIO = "DELETE FROM tabla_anuncios_venta WHERE id= %s; "

SQL_OBTENER_ANUNCIO = "SELECT ta.id, te.escala, tt.tipo, ta.titulo, ta.descripcion, ta.precio, ta.nomyapell, ta.email, ta.emailOK, ta.foto FROM tabla_anuncios_venta as ta, tabla_escalas as te, tabla_tipos as tt WHERE ta.id_escala = te.id AND ta.id_tipo = tt.id AND ta.id = %s; "
SQL_MODIFICAR_ANUNCIO = "UPDATE `tabla_anuncios_venta` SET `id_escala`= %s, `id_tipo`= %s, `titulo`=%s, `descripcion`= %s, `precio`=%s, `nomyapell`= %s, `email`= %s, `emailOK` = %s, `foto` = %s WHERE id = %s;"
SQL_MODIFICAR_SIN_IMAGEN = "UPDATE `tabla_anuncios_venta` SET `id_escala`= %s, `id_tipo`= %s, `titulo`=%s, `descripcion`= %s, `precio`=%s, `nomyapell`= %s, `email`= %s, `emailOK` = %s WHERE id = %s;"

SQL_LISTADO_ESCALA_TIPO = "SELECT ta.id, ta.fecha, te.escala, tt.tipo, ta.titulo, ta.descripcion, ta.precio, ta.nomyapell, ta.email, ta.emailOK, ta.foto FROM tabla_anuncios_venta as ta, tabla_escalas as te, tabla_tipos as tt WHERE ta.id_escala = te.id AND ta.id_tipo = tt.id AND ta.id_escala = %s AND ta.id_tipo = %s ORDER BY ta.id DESC;"

################   LISTADOS POR CATEGORIAS  ############################

SQL_LISTADO_TODOS_EMAILOK = "SELECT ta.id, ta.fecha, te.escala, tt.tipo, ta.titulo, ta.descripcion, ta.precio, ta.nomyapell, ta.email, ta.emailOK, ta.foto FROM tabla_anuncios_venta as ta, tabla_escalas as te, tabla_tipos as tt WHERE ta.id_escala = te.id AND ta.id_tipo = tt.id AND ta.emailOK = %s ORDER BY ta.id DESC;"
SQL_LISTADO_TIPO_EMAILOK =  "SELECT ta.id, ta.fecha, te.escala, tt.tipo, ta.titulo, ta.descripcion, ta.precio, ta.nomyapell, ta.email, ta.emailOK, ta.foto FROM tabla_anuncios_venta as ta, tabla_escalas as te, tabla_tipos as tt WHERE ta.id_escala = te.id AND ta.id_tipo = tt.id AND ta.id_tipo = %s AND ta.emailOK = %s ORDER BY ta.id DESC;"
SQL_LISTADO_ESCALA_EMAILOK = "SELECT ta.id, ta.fecha, te.escala, tt.tipo, ta.titulo, ta.descripcion, ta.precio, ta.nomyapell, ta.email, ta.emailOK, ta.foto FROM tabla_anuncios_venta as ta, tabla_escalas as te, tabla_tipos as tt WHERE ta.id_escala = te.id AND ta.id_tipo = tt.id AND ta.id_escala = %s AND ta.emailOK = %s ORDER BY ta.id DESC;"
SQL_LISTADO_ESCALA_TIPO_EMAILOK = "SELECT ta.id, ta.fecha, te.escala, tt.tipo, ta.titulo, ta.descripcion, ta.precio, ta.nomyapell, ta.email, ta.emailOK, ta.foto FROM tabla_anuncios_venta as ta, tabla_escalas as te, tabla_tipos as tt WHERE ta.id_escala = te.id AND ta.id_tipo = tt.id AND ta.id_escala = %s AND ta.id_tipo = %s AND ta.emailOK = %s ORDER BY ta.id DESC;"

################   CHAT  ############################################

SQL_INSERTAR_MENSAJE = "INSERT INTO tabla_mensajes (nombre,mensaje) VALUES (%s, %s);"
SQL_OBTENER_MENSAJES = "SELECT * FROM tabla_mensajes ORDER BY id DESC;"
SQL_INSERCION_REVISTA = "INSERT INTO `tabla_revistas` (`id`, `titulo`, `precio`, `tema`) VALUES (NULL, %s, %s, %s) ;"
# %s y % f es para indicar que esos campos van a ser variables para cada revista. Marca, DiezMinutos....etc
SQL_LISTADO_REVISTAS = "SELECT * FROM tabla_revistas ;"

SQL_BORRADO_REVISTA = "DELETE FROM tabla_revistas WHERE id = %s ;"

SQL_OBTENER_REVISTA = "SELECT * FROM tabla_revistas WHERE id = %s ;"

SQL_MODIFICAR_REVISTA = "UPDATE tabla_revistas SET titulo = %s, precio = %s, tema = %s WHERE id = %s ;"

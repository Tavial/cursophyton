'''
Escribir un programa que pregunte el nombre del usuario en la consola y después 
de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, 
donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras 
que tienen el nombre.

'''
nombre = str (input ("Introduce tu nombre "))
nombre_mayus = nombre.upper()
num_letras = len(nombre)
print (nombre_mayus+" tiene "+str(num_letras)+" letras (incluidos los espacios en blanco)")
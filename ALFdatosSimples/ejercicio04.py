'''
Escribir un programa que pregunte el nombre del usuario en la consola y un 
número entero e imprima por pantalla en líneas distintas el nombre del usuario 
tantas veces como el número introducido.

'''
nombre = str (input("Introduce tu nombre: "))
veces = int (input ("Introduce un número entero: "))
print (veces*(nombre+"\n")) #multiplico las veces por linea que quiero (nombre + cambio de línea)


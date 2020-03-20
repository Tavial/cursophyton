'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla 
si es par o impar.

'''

print ("*********************************************************")
print (" Este programa indica si un número entero es par o impar")
print ("*********************************************************")
print ("")
print ("Introduce un número entero: ")
numero = input ()
if numero.isspace() or numero.isalpha() or numero=="": #El valor introducido no es un espacio en blanco o una letra o no ha introducido nada
    print ("El valor introducido no es un número")
else:
    numero = int(numero)
    if numero % 2 == 0: # si el resto de dividir por 2 es 0, el número es par
        print ("El número introducido es par")
    else: 
        print ("El número introducido es impar")
    
    
    
    
    

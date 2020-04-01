'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla 
un triángulo rectángulo como el de más abajo, de altura el número introducido.

*
**
***
****
*****

'''

correcto = False
while not correcto:
    print ("Introduce un número entero mayor de 0: ")
    numero = input ()
    # filtramos que no se deje el número en blanco, o se meta un espacio o un 
    # carácter o un punto o una coma decimal
    if numero == "" or numero.isalnum() or numero.isspace() or numero.find(".") != -1 or numero.find(",") != -1:
        print ("El valor introducido no es correcto. Inténtalo de nuevo: ")
    else:
        numero = int (numero)
        if numero <= 0:
            print ("El valor introducido debe ser mayor que 0")
        else:
            correcto = True
print ("")
for i in range (numero): 
    print ((i+1)*"*")


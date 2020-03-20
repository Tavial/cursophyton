'''
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos 
ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que 
pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si 
el usuario tiene que tributar o no.

'''
print ("***************************************************************")
print (" Este programa averigua si un usuario tiene que tributar o no")
print ("***************************************************************")
print ("")
print ("Introduce tu edad: ")
edad = input()
print ("Introduce tus ingresos mensuales: ")
ingresos = input ()
if edad =="" or edad.isalpha() or edad.isspace() or ingresos =="" or ingresos.isalpha() or ingresos.isspace():
    print ("El valor introducido en alguno de los campos no es un número")
else: 
    edad = int(edad)
    ingresos = float(ingresos)
    if (edad > 16) and (ingresos >= 1000):
        print ("Tienes que tributar.")
    else:
        print ("No tienes que tributar.")
'''
Escribir un programa que pregunte al usuario su edad y muestre por pantalla si 
es mayor de edad o no.

'''
print ("***************************************************")
print ("Este programa te indica si eres mayor de edad o no")
print ("***************************************************")
print ("")
print ("Introduce tu edad: ")
edad = input ()
if edad.isalpha() or edad.isspace() or edad == "": # si edad es un carácter o un espacio en blanco o no ha introducido nada
    print ("No has introducido un número")
else: 
    edad = int(edad)
    if (edad >= 18) and (edad <= 120) :
        print ("Eres mayor de edad")
    elif (edad >= 0) and (edad < 18): 
        print ("Eres menor de edad")
    else: 
        print ("El número introducido no es un rango de edad válido")

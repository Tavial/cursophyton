'''
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y 
el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M 
y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir 
un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el 
grupo que le corresponde.

'''
print (" ******************************************************************* ")
print ("  Este grupo te clasifica en un grupo o otro según tu nombre y sexo ")
print (" ******************************************************************* ")
print ("")
print ("Introduce tu nombre: ")
nombre = input ()
print ("Introduce tu sexo (H/M): ")
sexo = input ()
if nombre.isdigit() or sexo.isdigit() or nombre.isspace() or sexo.isspace() or nombre =="" or sexo =="":
    print ("Alguno de los valores introducido no es correcto")
else: 
    sexo = sexo.lower() 
    nombre = nombre.lower()
    if (sexo != "h") and (sexo != "m"):
        print ("El valor introducido para el sexo no es el correcto")
    else: 
        if ((nombre < "m") and (sexo =="m")) or ((nombre > "n") and (sexo == "h")):
            print ("Perteneces al grupo A")
        else: 
            print ("Perteneces al grupo B")
            
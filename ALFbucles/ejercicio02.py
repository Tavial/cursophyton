'''
Escribir un programa que pregunte al usuario su edad y muestre por pantalla 
todos los años que ha cumplido (desde 1 hasta su edad).

'''

correcto = False
while not correcto:
    print ("Introduce tu edad: ")
    edad = input()
    if edad == "" or edad.isalnum() or edad.isspace() or edad.find(".") != -1 or edad.find(",") != -1:
        # la función find me permite detectar el punto decimal dentro de la cadena.
        # si lo encuentra da error porque si no el programa "casca" al intentar 
        # conventirlo a entero.
        print ("El valor introducido no es correcto. Inténtalo de nuevo ")
    else:
        correcto = True
edad = int (edad)    
for i in range (1,edad+1):
    print ("Has cumplido "+str(i)+" años")    
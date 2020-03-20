'''
Escribir un programa para una empresa que tiene salas de juegos para todas las 
edades y quiere calcular de forma automática el precio que debe cobrar a sus 
clientes por entrar. El programa debe preguntar al usuario la edad del cliente 
y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar 
gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

'''
print ("*****************************************")
print ("  Precio para acceder a sala de juegos ")
print ("*****************************************")
print ("")
print ("Introduce tu edad: ")
edad = input()
if edad == "" or edad.isspace() or edad.isalpha():
    print ("La edad introducidad no es un valor válido")
else: 
    edad = int (edad)
    if (edad >=0) and (edad < 4):
        print ("Puedes entrar gratis")
    elif (edad >= 4) and (edad < 18):
        print ("El precio de la entrada es 5 euros")
    elif (edad >= 18) and (edad <= 125):
        print ("El precio de la entrada es 10 euros")
    else: 
        print ("La edad introducida no es un número válido")
        
        

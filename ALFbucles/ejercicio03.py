'''
Escribir un programa que pida al usuario un número entero positivo y muestre por 
pantalla todos los números impares desde 1 hasta ese número separados por comas.

'''
correcto = False
while not correcto:
    print ("Introduce un número entero positivo: ")
    numero = input()
    if numero == "" or numero.isalnum() or numero.isspace() or numero.find(".") != -1 or numero.find(",") != -1:
        print ("El valor introducido no es correcto")
    else:
        numero = int (numero)
        if numero <= 0:
            print ("El valor introducido tiene que ser mayor que 0. Inténtalo de nuevo ")
        else: 
            correcto = True

for i in range (1,numero+1):
    if i % 2 != 0: #el numero es impar
        print (i,end=",")   
                

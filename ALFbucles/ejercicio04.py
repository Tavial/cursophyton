'''
Escribir un programa que pida al usuario un número entero positivo y muestre por 
pantalla la cuenta atrás desde ese número hasta cero separados por comas.

'''
import time
correcto = False
while not correcto: 
    print (" Introduce un número entero positivo ")
    numero = input()
    if numero == "" or numero.isalnum() or numero.isspace() or numero.find(".") != -1 or numero.find(",") != -1:
        print ("El valor introducido no es el correcto. Inténtalo de nuevo ")
    else: 
        numero = int (numero)
        if (numero <= 0):
            print ("El número introducido tiene que ser mayor que 0 ")
        else:
            correcto = True
print ("Cuenta atrás: ....")
for i in range (numero,-1,-1):
    time.sleep (1)
    print (i,end=",")
        
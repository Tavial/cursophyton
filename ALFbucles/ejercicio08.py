'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla 
un triángulo rectángulo como el de más abajo.

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1

'''

correcto = False
while not correcto: 
    print ("Introduce un número entero mayor que 0: ")
    numero = input ()
    if numero =="" or numero.isalnum() or numero.isspace() or numero.find(",") != -1 or numero.find(".") != -1:
        print ("El valor introducido no es correcto. Inténtalo de nuevo. ")
    else: 
        numero = int(numero)
        if numero < 0 :
            print ("El valor introducido debe ser mayor que 0. Inténtalo de nuevo. ")
        else: 
            correcto = True
print ("")
cadena = ""
for i in range (1,numero+1,2):
    for j in range (i,0,-2):
        cadena = cadena + " "+str(j)
        # Cuando i vale 1 j hace una sola vuelta con el valor 1 que se almacena en cadena
        # Cuando i vale 3 j hace dos vueltas valor 3 y 1 que almacena en cadena
        #...y así sucesivamente
    print (cadena)
    cadena= "" # inicializamos cadena a blanco para la cada vuelta de i (cada línea)
    
    
            

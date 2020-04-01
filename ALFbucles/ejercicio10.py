'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla 
si es un número primo o no.

algoritmo de número primo: Es aquel que solo es divisible por si mismo y por la unidad
Dividimos sucesivamente por 1,2,3... y paramos cuando el cociente es menor que el divisor

'''


correcto = False
while not correcto:
    print ("Introduce un número entero mayor que 0: ")
    numero = input ()
    if numero == "" or numero.isalnum() or numero.isspace() or numero.find(".") != -1 or numero.find(",") != -1:
        print ("El valor introducido no es correcto. Inténtalo de nuevo.")
    else:
        numero = int(numero)
        if numero <= 0:
            print ("El número introducido tiene que ser mayor que 0")
        else: 
            correcto = True
            primo = True
            divisor = 1
            cociente = 1
            while divisor<=numero and primo:
                resto = numero % divisor
                cociente = numero // divisor
                if resto == 0:
                    if divisor !=1 and divisor != numero:
                        # Todo numero es divisible por si mismo y la unidad. 
                        # tenemos que buscar otros divisores.
                        primo = False
                divisor += 1
            if primo:
                print ("El número "+str(numero)+" es primo.")
            else: 
                print ("El número "+str(numero)+" no es primo.") 
                        

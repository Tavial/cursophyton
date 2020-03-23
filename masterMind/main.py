'''
Escribe un programa que te permita jugar a una versión simplificada del juego 
Master Mind. El juego consistirá en adivinar una cadena de números distintos. 
Al principio, el programa debe pedir la longitud de la cadena (de 2 a 9 cifras). 
Después el programa debe ir pidiendo que intentes adivinar la cadena de números. 
En cada intento, el programa informará de cuántos números han sido acertados (el 
programa considerará que se ha acertado un número si coincide el valor y la 
posición).

'''
import random


def generaCadena (longitud):
    if longitud == 2:
        cad = random.randint (10,99)
    elif longitud == 3:
        cad = random.randint (100,999)
    elif longitud == 4:
        cad = random.randint (1000,9999)
    elif longitud == 5:
        cad = random.randint (10000,99999)
    elif longitud == 6:
        cad = random.randint (100000,999999)
    elif longitud == 7:
        cad = random.randint (1000000,9999999)
    elif longitud == 8:
        cad = random.randint (10000000,99999999)
    elif longitud == 9:
        cad = random.randint (100000000,999999999)
    return str(cad)
#end generaCadena

def adivinaCadena (mastermind):
    fin = False
    print (mastermind)
    adivinado = 0
    while not fin:
        correcto = False
        while not correcto:
            print ("Intenta adivinar la cadena: ")
            cadena = input ()
            if cadena =="" or cadena.isalpha() or cadena.isspace() or len(cadena) != len(mastermind):
                print ("El valor introducido no es correcto. Inténtalo de nuevo ")
            else:
                correcto=True
        
        for i in range (len(mastermind)):
            if mastermind [i] == cadena [i]:
                adivinado +=1
        
        if adivinado == len (mastermind): #Ha adivinado la cadena
            fin = True
            print ("Enhorabuena. Con "+cadena+" has adivinado los "+str(adivinado)+" valores")
            print ("")
            print ("¿Quieres jugar otra vez? (s/n)")
            seguir = input()
            seguir = seguir.lower()
            while seguir == "" or seguir.isspace() or seguir.isdigit() or ((seguir != "s") and (seguir != "n")): 
                print ("El valor introducido no es correcto.")
                seguir = input ("¿quieres seguir jugando? (s/n): ")
                seguir = seguir.lower()
            if seguir == "s":
                return False
            else:
                return True
        else:
            print ("Con "+cadena+" has adivinado "+str(adivinado)+" valores")
            adivinado = 0
            
        

    

#end adivinaCadena    


            

fin_juego = False
while not fin_juego:
    print ("Introduce la longitud de cadena de números a adivinar (2 a 9 cifras): ")
    longitud = input ()
    correcto = False
    while not correcto:
        if longitud =="" or longitud.isalpha() or longitud.isspace():
            print ("El valor introducido no es correcto. Inténtalo de nuevo ")
            longitud = input()
        else:
            longitud = int (longitud)
            if longitud >= 2 and longitud <= 9:
                correcto = True
            else:
                print ("El valor numérico introducido no es correcto. Inténtalo de nuevo ")
                longitud = input()
    mastermind = generaCadena (longitud) #una vez que la longitud sea correcta generamos la cadena
    fin_juego = adivinaCadena(mastermind)
    
    
            

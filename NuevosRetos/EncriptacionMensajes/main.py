'''
Reto 5 - Encriptación de mensajes

El cifrado Vigenère es un cifrado basado en diferentes series de caracteres o letras del cifrado César 
formando estos caracteres una tabla, llamada tabla de Vigenère, que se usa como clave. El cifrado de 
Vigenère es un cifrado de sustitución simple polialfabético.

1) Vamos a encriptar el mensaje TATIANA utilizando como palabra clave NENA. Lo primero, ponemos nuestro alfabeto 
castellano de la siguiente forma:

-------------------------------------------------------------------------------------------------------------
| A | B | C | D | E | F | G | H | I | J | K | L | M | N | Ñ | O | P | Q | R | S | T | U | V | W | X | Y | Z | 
|------------------------------------------------------------------------------------------------------------
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |10| 11| 12| 13| 14| 15| 16| 17| 18| 19| 20| 21| 22| 23| 24| 25| 26 |
-------------------------------------------------------------------------------------------------------------

N = 13
E = 4
N = 13
A = 0

-----------------------------
| T | A | T | I | A | N | A |
|-------------------------- |
|13| 4 | 13| 0 | 13| 4 | 13 |
-----------------------------

Se le suma ese valor a su letra original con lo que se desplazan a la derecha ese número.

T = 13 + 20 = 33 -> Nueva Letra = G
A = 4 + 0 = 4 -> Nueva letra = E
T = 13 + 20 = 33 -> Nueva letra = G
I = 0 + 8 = 8 -> Nueva letra = I
A = 13 + 0 = 13 -> Nueva letra = N
N = 4 + 13 = 17 -> Nueva letra = Q
A = 13 + 0 = 13 -> Nueva letra = N


Es en resumen el funcionamiento de este método.
 

'''

from modulos import criptografia
# -*- coding: utf-8 -*-
import codecs;

caracteres_especiales = [" ",".",",",":",";","'",'"',"-","_","{","}","[","]","¿","?","=",")","(","/","&","%","$","#","·","@","¡","!","|","º","ª","\\","<",">","0","1","2","3","4","5","6","7","8","9","`","*","+","Ç","ç"]
vigenere = criptografia.Vigenere()
cuadro_vigenere = vigenere.rellenarCuadro()
correcto = False
salir = False
while not salir:  

    print (" =============================================================== ")
    print (" ||   BIENVENIDO AL PROGRAMA DE CIFRADO Y DESCIFRADO VIGENERE ||")
    print (" ==============================================================")
    print ("")
    print (" 1  CIFRADO")
    print (" 2  DESCIFRADO")
    print (" 3  SALIR")
    print ("")
    print ("Introduce la opcion:")
    correcto = False
    while not correcto: 
        opcion = str(input ())
        if opcion != "1" and opcion !="2" and opcion !="3":
            correcto = False
        else:
            correcto = True
    if opcion == "1":
        print ("")
        correcto = False
        while not correcto: 
            clave = input ("Introduzca la palabra clave de cifrado: ")
            if not clave.isalpha() or clave.isspace():
                correcto = False
            else: 
                correcto = True   
        archivo_entrada = codecs.open ("origen.txt","r","utf8")
        archivo_salida = codecs.open ("encriptado.txt","a","utf8")
        puntero_clave = 0
        for renglon in archivo_entrada:
            #print (renglon)
            puntero_renglon = 0
            tope = len (clave)-1
            cadena_encriptada = ""
            while renglon[puntero_renglon] !="\n" and renglon[puntero_renglon] !="\r" and puntero_renglon <=len(renglon)-2:
                if renglon[puntero_renglon] not in caracteres_especiales:
                    valor_clave = clave[puntero_clave]
                    valor_renglon = renglon[puntero_renglon]
                    valor_encriptado = vigenere.encriptar (cuadro_vigenere,valor_clave,valor_renglon)
                    cadena_encriptada = cadena_encriptada + valor_encriptado
                    puntero_clave += 1
                    puntero_renglon += 1
                    if puntero_clave > tope:
                        puntero_clave = 0 
                else:
                    cadena_encriptada = cadena_encriptada + renglon[puntero_renglon]
                    puntero_renglon += 1
                    if puntero_clave > tope:
                        puntero_clave = 0 
            archivo_salida.write(cadena_encriptada+"\n") 
        print ("operación de encriptado finalizada")
        archivo_entrada.close()
        archivo_salida.close()
    elif opcion == "2":
        print ("")
        correcto = False
        while not correcto: 
            clave = input ("Introduzca la palabra clave de descifrado: ")
            if not clave.isalpha() or clave.isspace():
                correcto = False
            else: 
                correcto = True   
        archivo_entrada = codecs.open ("encriptado.txt","r","utf8")
        archivo_salida = codecs.open ("vuelta_al_origen.txt","a","utf8")
        puntero_clave = 0
        for renglon in archivo_entrada:
            puntero_renglon = 0
            tope = len (clave)-1
            cadena_desencriptada = ""
            while renglon[puntero_renglon] !="\n" and renglon[puntero_renglon] !="\r" and puntero_renglon <len(renglon)-1:
                if renglon[puntero_renglon] not in caracteres_especiales:
                    valor_clave = clave[puntero_clave]
                    valor_renglon = renglon[puntero_renglon]
                    valor_desencriptado = vigenere.desencriptar (cuadro_vigenere,valor_clave,valor_renglon)
                    cadena_desencriptada = cadena_desencriptada + valor_desencriptado
                    puntero_clave += 1
                    puntero_renglon += 1
                    if puntero_clave > tope:
                        puntero_clave = 0 
                else:
                    cadena_desencriptada = cadena_desencriptada + renglon[puntero_renglon]
                    puntero_renglon += 1
                    if puntero_clave > tope:
                        puntero_clave = 0 
            archivo_salida.write(cadena_desencriptada+"\n") 
        print ("operación de desencriptado finalizada")

        archivo_entrada.close()
        archivo_salida.close()
    else:
        print ("Muchas gracias por usar nuestro programa")
        salir = True
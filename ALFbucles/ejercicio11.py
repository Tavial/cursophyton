'''
Escribir un programa que pida al usuario una palabra y luego muestre por 
pantalla una a una las letras de la palabra introducida empezando por la última.

'''
correcto = False
while not correcto:
    print ("Introduce una palabra: ")
    palabra = input()
    if palabra == "" or palabra.isspace():
        print ("Tienes que introducir una palabra. Inténtalo de nuevo")
    else:
        correcto = True

for letra in range (len(palabra)-1,-1,-1):
    print (palabra[letra])
        
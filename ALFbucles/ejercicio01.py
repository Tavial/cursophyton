'''
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

'''
correcto = False
while not correcto:
    print ("Introduce una palabra: ")
    palabra = input ()
    if palabra =="" or palabra.isspace():
        print ("No has introducido nada por teclado. Inténtalo de nuevo")
    else:
        correcto = True
for i in range (10):
    print (palabra)

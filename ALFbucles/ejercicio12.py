'''
Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
y muestre por pantalla el número de veces que aparece la letra en la frase.

'''

correcto = False
while not correcto: 
    print ("Introduce una frase: ")
    frase = input ()
    if frase == "" or frase.isspace():
        #no permitimos que la frase solo tenga espacios en blanco o esté vacía.
        print ("No has introducido nada. Inténtalo de nuevo. ")
    else:
        correcto = True
frase = frase.lower() # lo pasamos a minúscula
correcto = False
while not correcto: 
    print ("Introduce una letra: ")
    letra = input ()
    #no permitimos que en la letra se introduzca sólo espacios o esté en blanco o sea un número o que sea más de una carácter
    if letra =="" or letra.isspace() or len(letra) != 1 or letra.isdigit():
        print ("El valor introducido no es el correcto. Inténtalo de nuevo ")
    else:
        correcto = True
letra = letra.lower() #
contador = 0        
for l in range (0,len(frase)):
    if letra == frase[l]:
        contador += 1
print ("El número de veces que aparece la letra "+letra+" en la frase es "+str(contador)+" veces")




'''
Escribir un programa que pida al usuario dos números enteros y muestre por 
pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son 
los números introducidos por el usuario, y <c> y <r> son el cociente y el resto 
de la división entera respectivamente.

'''
print ("Vamos a obtener el cociente y el resto de dos números enteros")
print("")
n = int (input("Introduce un número entero: "))
m = int (input("Introduce otro número entero: "))
c = int (n / m)
r = n % m
print ("El cociente de la división es: "+str(c))
print ("El resto de la división es: "+str(r))
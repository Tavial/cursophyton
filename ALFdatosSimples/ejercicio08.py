'''
Escribir un programa que lea un entero positivo, 𝑛, introducido por el usuario y 
después muestre en pantalla la suma de todos los enteros desde 1 hasta 𝑛. La 
suma de los 𝑛 primeros enteros positivos puede ser calculada de la siguiente 
forma:

suma= n*(n+1) / 2

'''

n = int (input("Introduce un valor entero positivo: "))
suma = (n * (n+1))/2
print (" La suma de los "+str(n)+" primeros enteros es: "+ str(suma))

'''
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.

'''
print (" ******************************** ")
print (" *    TABLA DE MULTIPLICAR      * ")
print (" ******************************** ")
print ("")
for i in range (1,11):
    print ("Tabla del "+str(i))
    print ("--------------")
    for j in range (1,11):
        print (str(i)+" x "+str(j)+" = "+str (i*j))
    print ("")
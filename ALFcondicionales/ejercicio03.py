'''
Escribir un programa que pida al usuario dos números y muestre por pantalla su 
división. Si el divisor es cero el programa debe mostrar un error.

'''
print ("**************************************************")
print (" Este programa muestra la división de dos números")
print ("**************************************************")
print ("")
print ("Introduce el dividendo: ")
dividendo = input ()
print ("Introduce el divisor: ")
divisor = input ()
if dividendo.isalpha() or divisor.isalpha() or dividendo.isspace() or divisor.isspace()or dividendo == "" or divisor == "":
    print ("El dividendo o divisor introducido no es un numero")
else: 
    dividendo = float(dividendo)
    divisor = float (divisor)
    if divisor == 0:
        print ("Estás tratando de dividir "+str(dividendo)+" entre 0")
    else:
        cociente = round ((dividendo/divisor),2)
        print ("El cociente de la división es: "+str(cociente))
        
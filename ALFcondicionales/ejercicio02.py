'''
Escribir un programa que almacene la cadena de caracteres contraseña en una 
variable, pregunte al usuario por la contraseña e imprima por pantalla si la 
contraseña introducida por el usuario coincide con la guardada en la variable 
sin tener en cuenta mayúsculas y minúsculas.

'''
password = "password"
print ("Introduce contraseña: ")
passwd = input ()
if passwd =="": #comprobamos que el usuario haya introducido algún carácter
    print ("No has introducido ninguna contraseña")
else: 
    passwd = passwd.lower() #convertimos la cadena a minúsculas
    if password == passwd:
        print ("ACCESO OK. Bienvenido!!")
    else:
        print ("ACCESO DENEGADO. Contraseña incorrecta")

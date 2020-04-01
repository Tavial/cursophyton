'''
Escribir un programa que almacene la cadena de caracteres contraseña en una 
variable, pregunte al usuario por la contraseña hasta que introduzca la 
contraseña correcta.

'''

password = "Contraseña"
correcto = False
while not correcto: 
    print ("Introduzca la contraseña: ")
    contrasena = input()
    if contrasena =="" or contrasena.isspace():
        print ("Tienes que introducir algún valor. Inténtalo de nuevo")
    else:
        if contrasena == password:
            print ("Enhorabuena. Has acertado la contraseña ")
            correcto = True
        else:
            print ("No es la contraseña correcta. Inténtalo de nuevo ")
        
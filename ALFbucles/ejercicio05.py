'''
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés 
anual y el número de años, y muestre por pantalla el capital obtenido en la 
inversión cada año que dura la inversión.

'''

correcto = False
while not correcto: # controlamos que los valores introducidos sean correctos
    correcto = True
    print ("Introduce la cantidad a invertir: ")
    capital = input ()
    print ("Introduce el interés anual de la inversión: ")
    interes = input ()
    print ("Introduce el número de años de la inversión: ")
    anyos = input ()
    if capital == "" or capital.isalpha() or capital.isspace() or capital.find(",")!=-1:
        print ("El valor del capital no es correcto. Inténtalo de nuevo ")
        correcto = False
    else:
        capital = float(capital)
    if interes == "" or interes.isalpha() or interes.isspace() or interes.find(",")!=-1:
        print ("El valor del interes no es correcto. Inténtalo de nuevo ")
        correcto = False
    else:
        interes = float (interes) 
    if anyos == "" or anyos.isalpha() or anyos.isspace() or anyos.find(".") != -1 or anyos.find(",") != -1:
        print ("El valor de número de años no es correcto. Inténtalo de nuevo ")
        correcto = False   
    else:
        anyos = int (anyos)
    if correcto:
        if capital <= 0:
            print ("El capital tiene que ser mayor que 0")
            correcto = False
        else:
            correcto =True
        if anyos <= 0:
            print ("El número de años tiene que ser mayor que 0")
            correcto = False
        else:
            correcto = True
# calculamos el capital año por año             
for i in range (1,anyos+1):
    capital = round ((capital+((capital*interes*i)/100)),2)
    print ("Capital en el año "+str(i)+": "+str(capital)+" euros")  
    
    
    
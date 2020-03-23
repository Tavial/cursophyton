'''
Calculadora básica con Tkinter

'''
from tkinter import *
from tkinter import messagebox


x = 0
y = 0
pantalla ="0"
operacion =""
entero = True
punto = False
negativo = False

def borrarPantalla ():
    canvas.create_rectangle (32, 28, 320, 78, fill ="white", width=4)

#end borrarPantalla

###########################################################

def mostrarPantalla (pantalla):
    borrarPantalla ()
    x1 = 310
    for i in range (len(pantalla)-1):
        x1 = x1 - 6
    canvas.create_text(x1,51,font=("verdana",14),text=pantalla)
    
# end mostrarPantalla

#############################################################   

def click_raton (evento):
    global x,y,pantalla,operacion,entero, operador1, operador2,punto, negativo 
    # Se pone global para poder usar las variables
    # x e y definidas fuera de la funcion
    x = evento.x
    y = evento.y
    print("x: " + str(x))
    print("y: " + str(y))
    digito = False
    if (x >= 29 ) and (x <= 167) and (y >= 364) and (y <= 412):
        #pulsamos 0
        caracter="0"
        digito = True
    elif (x >= 29 ) and (x <= 92) and (y >= 304) and (y <= 352):
        #pulsamos 1
        caracter="1"
        digito = True
    elif (x >= 104 ) and (x <= 167) and (y >= 304) and (y <= 352):
        #pulsamos 2
        caracter="2"
        digito = True
    elif (x >= 178 ) and (x <= 245) and (y >= 304) and (y <= 352):
        #pulsamos 3
        caracter="3"
        digito = True
    elif (x >= 29 ) and (x <= 92) and (y >= 243) and (y <= 292):
        #pulsamos 4
        caracter="4"
        digito = True
    elif (x >= 104 ) and (x <= 167) and (y >= 243) and (y <= 292):
        #pulsamos 5
        caracter="5"
        digito = True
    elif (x >= 178 ) and (x <= 245) and (y >= 243) and (y <= 292):
        #pulsamos 6
        caracter="6"
        digito = True
    elif (x >= 29 ) and (x <= 92) and (y >= 184) and (y <= 232):
        #pulsamos 7
        caracter="7"
        digito = True
    elif (x >= 104 ) and (x <= 167) and (y >= 184) and (y <= 232):
        #pulsamos 8
        caracter="8"
        digito = True
    elif (x >= 178 ) and (x <= 245) and (y >= 184) and (y <= 232):
        #pulsamos 9
        caracter="9" 
        digito = True 
    elif (x >= 29 ) and (x <= 92) and (y >= 123) and (y <= 172):
        #pulsamos C
        #borramos la pantalla e inicializamos la cadena a 0 
        digito = False
        borrarPantalla()
        pantalla ="0"
        mostrarPantalla (pantalla)
    elif (x >= 257 ) and (x <= 318) and (y >= 243) and (y <= 292):
        #pulsamos +
        digito = False
        operacion = "suma"
        #borramos pantalla
        borrarPantalla()
        operador1 = pantalla # volcamos en el operador1 el contenido de la pantalla
        pantalla = "0"
        mostrarPantalla (pantalla)
    elif (x >= 257 ) and (x <= 318) and (y >= 184) and (y <= 232):  
        #pulsamos -
        digito = False
        operacion ="resta"
        #borramos pantalla
        borrarPantalla()
        operador1 = pantalla # volcamos en el operador1 el contenido de la pantalla
        pantalla ="0"
        mostrarPantalla (pantalla)
    elif (x >= 257 ) and (x <= 318) and (y >= 123) and (y <= 172): 
        #pulsa x
        digito = False
        operacion = "multiplicacion"
        #borramos pantalla
        borrarPantalla()
        operador1 = pantalla # volcamos en el operador1 el contenido de la pantalla
        pantalla ="0"
        mostrarPantalla (pantalla)
    
    elif (x >= 178 ) and (x <= 245) and (y >= 123) and (y <= 172): 
        #pulsa /
        digito = False
        operacion = "division"
        #borramos pantalla
        borrarPantalla()
        operador1 = pantalla # volcamos en el operador1 el contenido de la pantalla
        pantalla ="0"
        mostrarPantalla (pantalla)
    
    elif (x >= 182 ) and (x <= 245) and (y >= 364) and (y <= 412): 
        #pulsa . decimal
        caracter="."
        digito = True
        punto = True
        entero = False
    
    elif (x >= 104) and (x <= 167) and (y >= 123) and (y <= 172): 
        #pulsa +/-
        caracter="-"
        digito = True
        negativo = True
    
    elif (x >= 257 ) and (x <= 318) and (y >= 304) and (y <= 412):
        #pulsamos =
        digito = False
        #borramos pantalla
        borrarPantalla()
        operador2 = pantalla #volcamos en el operador2 el contenido de la pantalla
        if (operacion == "suma"):
            if entero: #Hacemos la suma entera
                operador1 = int(operador1)
                operador2 = int(operador2)
                suma = operador1+operador2
            elif not entero: #Hacemos la suma real
                operador1 = float(operador1)
                operador2 = float (operador2)
                suma = operador1+operador2
            pantalla = str (suma)
           
        elif (operacion =="resta"):
            if entero: #Hacemos la resta entera
                operador1 = int(operador1)
                operador2 = int(operador2)
                resta = operador1-operador2
            elif not entero: #Hacemos la resta real
                operador1 = float(operador1)
                operador2 = float (operador2)
                resta = operador1-operador2
            pantalla = str (resta)
            
        elif (operacion =="multiplicacion"):
            if entero: #Hacemos la multiplicacion entera
                operador1 = int(operador1)
                operador2 = int(operador2)
                producto = operador1*operador2
            elif not entero: #Hacemos la resta real
                operador1 = float(operador1)
                operador2 = float (operador2)
                producto = round ((operador1*operador2),2)
            pantalla = str (producto)
        
        elif (operacion =="division"):
            if entero: #Hacemos la multiplicacion entera
                operador1 = int(operador1)
                operador2 = int(operador2)
                cociente = operador1/operador2
            elif not entero: #Hacemos la resta real
                operador1 = float(operador1)
                operador2 = float (operador2)
                cociente = round ((operador1*operador2),2)
            pantalla = str (cociente)
        
        mostrarPantalla(pantalla)
        entero=True
        
             
    
    if digito:   
        if pantalla =="0":
            if not punto: 
                pantalla=caracter
            else: 
                pantalla=pantalla+caracter
                punto = False
        else:
            if len(pantalla) < 20:
                if negativo:
                    if pantalla[0]=="-": #El número es negativo. Lo pasamos a positivo
                        pantalla = pantalla.strip("-")       
                    else:
                        pantalla=caracter+pantalla
                    negativo=False
                else: 
                    pantalla = pantalla+caracter
            else: 
                messagebox.showinfo(title = "información", message ="Sólo se admiten operaciones de menos de 20 dígitos")
        mostrarPantalla (pantalla)
       
    
    
    

calculadora = Tk() #creamos una ventana calculadora
canvas = Canvas(calculadora, width = 348, height = 435 )
canvas.pack (expand = YES, fill = BOTH)

imagen = PhotoImage (file="fondo.png") #cargamos la imagen de la calculadora
canvas.create_image(0,0,image = imagen, anchor = NW) # En este método indicamos donde queremos que se pinte la imagen
#NW Orientación noroeste. Es un acuerdo suyo de Tkinter.

calculadora.geometry("348x435")
calculadora.title ("CALCULADORA Estándar")
canvas.create_text(310,51,font=("verdana",14),text="0")
# La función del clic de ratón hay que asignárselo al CANVAS
# o a la ventana.
calculadora.bind("<Button 1>", click_raton) #clic izquierdo del raton

calculadora.mainloop()
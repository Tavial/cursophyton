'''
Encontrar las 8 diferencias entre dos imágenes

'''
############   IMPORTACIONES DE PAQUETES    #########################
from tkinter import messagebox
from tkinter import *
import time

# inicializamos las coordenadas x e y a 0
x = 0
y = 0 
diferencias = [False, False, False, False, False, False, False, False]
aciertos = 0
fin_juego = False
tiempof = 0

def click_raton (evento): 
    global x,y # las definimos de forma global para poder usarlas fuera de la función
    # Ahora igualamos las variables al valor que van a tomar cuando se haga click
    # con el ratón (evento) 
    global aciertos, tiempof, nombre
    x = evento.x
    y = evento.y
    # Mostramos el valor de x e y cuando hacemos click en el ratón
    print ("coordenada x "+str(x)) 
    print ("coordenada y "+str(y)) 
    if aciertos < 8 or not fin_juego: #no lo hemos acertado todo
        if (x >= 1006 and x <= 1148 and y >= 46 and y <= 108):
            if diferencias[0]==False:
                messagebox.showinfo(title = "¡¡ACIERTO!!", message ="Has encontrado una diferencia. Te quedan "+str (7-aciertos)+" diferencias por encontrar")
                canvas.create_rectangle (1096, 46, 1148, 108, width=4)
                diferencias [0] = True
                aciertos += 1
                if aciertos == 8:
                    tiempof= time.time ()
                    total = round ((tiempof - tiempo0),2)
                    messagebox.showinfo(title = "FIN DEL JUEGO", message = "Enhorabuena!!. Has encontrado las 8 diferencias en "+str (total)+" segundos")
                    fichero = open ("ranking.txt","a") 
                    frase = "Jugador: "+nombre+" ---> "+"Tiempo: "+str(total)
                    fichero.write ("\n"+frase)
                    fichero.close ()
                    fin_juego = True
            else: #ya se ha pinchado en esa zona
                messagebox.showinfo(title = "DIFERENCIA YA ENCONTRADA", message = "Ya has encontrado esa diferencia")            
        elif (x >= 1067 and x <= 1090 and y >= 517 and y <= 570):
            if diferencias[1]==False:
                messagebox.showinfo(title = "¡¡ACIERTO!!", message ="Has encontrado una diferencia. Te quedan "+str (7-aciertos)+" diferencias por encontrar")
                canvas.create_rectangle (1067, 517, 1090, 570, width=4)
                diferencias [1] = True
                aciertos += 1
                if aciertos == 8:
                    tiempof= time.time ()
                    total = round ((tiempof - tiempo0),2)
                    messagebox.showinfo(title = "FIN DEL JUEGO", message = "Enhorabuena!!. Has encontrado las 8 diferencias en "+str (total)+" segundos")
                    fichero = open ("ranking.txt","a") 
                    frase = "Jugador: "+nombre+" ---> "+"Tiempo: "+str(total)
                    fichero.write ("\n"+frase)
                    fichero.close ()
                    fin_juego = True
            else: #ya se ha pinchado en esa zona
                messagebox.showinfo(title = "DIFERENCIA YA ENCONTRADA", message = "Ya has encontrado esa diferencia")  
        elif (x >= 1150 and x <= 1190 and y >= 246 and y <= 264):
            if diferencias[2]==False: 
                messagebox.showinfo(title = "¡¡ACIERTO!!", message ="Has encontrado una diferencia. Te quedan "+str (7-aciertos)+" diferencias por encontrar")
                canvas.create_rectangle (1150, 246, 1190, 264, width=4)
                diferencias [2] = True
                aciertos += 1
                if aciertos == 8:
                    tiempof= time.time ()
                    total = round ((tiempof - tiempo0),2)
                    messagebox.showinfo(title = "FIN DEL JUEGO", message = "Enhorabuena!!. Has encontrado las 8 diferencias en "+str (total)+" segundos")
                    fichero = open ("ranking.txt","a") 
                    frase = "Jugador: "+nombre+" ---> "+"Tiempo: "+str(total)
                    fichero.write ("\n"+frase)
                    fichero.close ()
                    fin_juego = True
            else: #ya se ha pinchado en esa zona
                messagebox.showinfo(title = "DIFERENCIA YA ENCONTRADA", message = "Ya has encontrado esa diferencia") 
        elif (x >= 775 and x <= 832 and y >= 511 and y <= 533):
            if (diferencias[3] == False):
                messagebox.showinfo(title = "¡¡ACIERTO!!", message ="Has encontrado una diferencia. Te quedan "+str (7-aciertos)+" diferencias por encontrar")
                canvas.create_rectangle (775, 511, 832, 533, width=4)
                diferencias [3] = True
                aciertos += 1
                if aciertos == 8:
                    tiempof= time.time ()
                    total = round ((tiempof - tiempo0),2)
                    messagebox.showinfo(title = "FIN DEL JUEGO", message = "Enhorabuena!!. Has encontrado las 8 diferencias en "+str (total)+" segundos")
                    fichero = open ("ranking.txt","a") 
                    frase = "Jugador: "+nombre+" ---> "+"Tiempo: "+str(total)
                    fichero.write ("\n"+frase)
                    fichero.close ()
                    fin_juego = True
            else: #ya se ha pinchado en esa zona
                messagebox.showinfo(title = "DIFERENCIA YA ENCONTRADA", message = "Ya has encontrado esa diferencia") 
        elif (x >= 1034 and x <= 1061 and y >= 623 and y <= 704):
            if (diferencias[4] == False):
                messagebox.showinfo(title = "¡¡ACIERTO!!", message ="Has encontrado una diferencia. Te quedan "+str (7-aciertos)+" diferencias por encontrar")
                canvas.create_rectangle (1034, 623, 1061, 704, width=4)
                diferencias [4] = True 
                aciertos += 1
                if aciertos == 8:
                    tiempof= time.time ()
                    total = round ((tiempof - tiempo0),2)
                    messagebox.showinfo(title = "FIN DEL JUEGO", message = "Enhorabuena!!. Has encontrado las 8 diferencias en "+str (total)+" segundos")
                    fichero = open ("ranking.txt","a") 
                    frase = "Jugador: "+nombre+" ---> "+"Tiempo: "+str(total)
                    fichero.write ("\n"+frase)
                    fichero.close ()
                    fin_juego = True
            else: #ya se ha pinchado en esa zona
                messagebox.showinfo(title = "DIFERENCIA YA ENCONTRADA", message = "Ya has encontrado esa diferencia") 
        elif (x >= 1202 and x <= 1265 and y >= 556 and y <= 610):
            if (diferencias[5] == False):
                messagebox.showinfo(title = "¡¡ACIERTO!!", message ="Has encontrado una diferencia. Te quedan "+str (7-aciertos)+" diferencias por encontrar")
                canvas.create_rectangle (1202, 556, 1265, 610, width=4)
                diferencias [5] = True 
                aciertos += 1
                if aciertos == 8:
                    tiempof= time.time ()
                    total = round ((tiempof - tiempo0),2)
                    messagebox.showinfo(title = "FIN DEL JUEGO", message = "Enhorabuena!!. Has encontrado las 8 diferencias en "+str (total)+" segundos")
                    fichero = open ("ranking.txt","a") 
                    frase = "Jugador: "+nombre+" ---> "+"Tiempo: "+str(total)
                    fichero.write ("\n"+frase)
                    fichero.close ()
                    fin_juego = True
            else: #ya se ha pinchado en esa zona
                messagebox.showinfo(title = "DIFERENCIA YA ENCONTRADA", message = "Ya has encontrado esa diferencia") 
        elif (x >= 950 and x <= 969 and y >= 403 and y <= 428):
            if (diferencias[6] == False):
                messagebox.showinfo(title = "¡¡ACIERTO!!", message ="Has encontrado una diferencia. Te quedan "+str (7-aciertos)+" diferencias por encontrar") 
                canvas.create_rectangle (950, 403, 969, 428, width=4)
                diferencias [6] = True 
                aciertos += 1
                if aciertos == 8:
                    tiempof= time.time ()
                    total = tiempof - tiempo0
                    messagebox.showinfo(title = "FIN DEL JUEGO", message = "Enhorabuena!!. Has encontrado las 8 diferencias en "+str (total)+" segundos")
                    fichero = open ("ranking.txt","a") 
                    frase = "Jugador: "+nombre+" ---> "+"Tiempo: "+str(total)
                    fichero.write ("\n"+frase)
                    fichero.close ()
                    fin_juego = True
            else: #ya se ha pinchado en esa zona
                messagebox.showinfo(title = "DIFERENCIA YA ENCONTRADA", message = "Ya has encontrado esa diferencia") 
        elif (x >= 998 and x <= 1029 and y >= 400 and y <= 424):
            if (diferencias[7] == False):
                messagebox.showinfo(title = "¡¡ACIERTO!!", message ="Has encontrado una diferencia. Te quedan "+str (7-aciertos)+" diferencias por encontrar")
                canvas.create_rectangle (998, 400, 1029, 424, width=4)
                diferencias [7] = True 
                aciertos += 1
                if aciertos == 8:
                    tiempof= time.time ()
                    total = round ((tiempof - tiempo0),2)
                    messagebox.showinfo(title = "FIN DEL JUEGO", message = "Enhorabuena!!. Has encontrado las 8 diferencias en "+str (total)+" segundos")
                    fichero = open ("ranking.txt","a") 
                    frase = "Jugador: "+nombre+" ---> "+"Tiempo: "+str(total)
                    fichero.write ("\n"+frase)
                    fichero.close ()
                    fin_juego = True
            else: #ya se ha pinchado en esa zona
                messagebox.showinfo(title = "DIFERENCIA YA ENCONTRADA", message = "Ya has encontrado esa diferencia")
        else: #no ha pinchado en ninguna de las áreas donde están las diferencias
            messagebox.showinfo(title = "NO HAY DIFERENCIA", message = "Donde has pinchado no hay ninguna diferencia")
             
    else: 
        tiempof= time.time ()
        total = round ((tiempof - tiempo0),2)
        messagebox.showinfo(title = "FIN DEL JUEGO", message = "Enhorabuena!!. Has encontrado las 8 diferencias en "+str (total)+" segundos")
        
# fin def click_raton

def okRanking ():
    ranking.withdraw()
    ranking.destroy()

def listarRanking ():
    global ranking, canvas2
    ranking = Tk () # Creamos la ventana para listar los rankings 
    canvas2 = Canvas (ranking, width= 300, height = 600)
    canvas2.pack (expand = YES, fill = BOTH )
    ranking.geometry("300x600")
    ranking.title ("Mejores puntuaciones")
    fichero = open ("ranking.txt","r")
    x1 = 100
    y1 = 50
    for linea in fichero:
        y1=y1+20
        canvas2.create_text(x1,y1,text=linea)     
    fichero.close()
    botonOK = Button (ranking,text="OK",command=okRanking).place (x=150,y=525)
    ranking.mainloop()
    ventanaPrincipal()
        


def ventanaPrincipal ():
    global ventana, tiempo0, canvas
    ventana = Tk () # Creamos el objeto ventana de la clase Tk (tkinter)
    tiempo0 = time.time()

    # ahora vamos a definir un canvas (lienzo) sobre la ventana

    canvas = Canvas (ventana, width=1338, height = 716)
    # ahora posicionamos el canvas con el método pack
    # expand = YES quiere decir que el canvas se expande con la ventana
    # fill = BOTH quiere decir que el canvas rellena todo el espacio vertical y
    # horizontal de la ventana
    canvas.pack (expand = YES, fill = BOTH )

    imagen = PhotoImage (file = "juegoDiferencias.png") #cargamos la imagen

    # y la ponemos en el canvas
    # En este método indicamos donde queremos que se pinte la imagen
    # NW Orientación noroeste. Es un acuerdo propio del método de Tkinter.
    canvas.create_image(0,0,image = imagen, anchor = NW)

    # fijamos las dimensiones de la ventana. Le vamos a poner las mismas que el lienzo
    ventana.geometry("1338x716")

    ventana.title ("Haz click en la imagen derecha para descubrir las 8 diferencias")
    messagebox.showinfo(title = "INSTRUCCIONES", message="Debes encontrar en el dibujo de la derecha las 8 diferencias en el menor tiempo posible")


    # vinculamos la acción de pulsar el botón izquierdo con nuestra funcion que se 
    # ejecutará cada vez que se haga un clic
    ventana.bind ("<Button-1>",click_raton) 

    # El método mainloop mantiene visible la ventana raíz.
    # Si se elimina esta línea la ventana no se mantendrá visible    
    ventana.mainloop()
    # Siempre el código debe terminar con el método mainloop.
#end def ventanaPrincipal
        

def ok():
    global nombre
    nombre = entradaNombre.get()
    print (nombre)
    if nombre !="":
        messagebox.showinfo("Información", "Has introducido el nombre correctamente")
        emergente.destroy()
        listarRanking()
    else: 
        messagebox.showinfo("Información", "No has introducido nada")
        

emergente = Tk () # Creamos el objeto ventana emergente de la clase Tk (tkinter)
emergente.geometry("250x100+300+300")
emergente.title ("Introducir nombre")
etiquetaNombre=Label(emergente, text="Nombre").place (x=10,y=10)
entradaNombre = StringVar()
name = Entry(emergente,textvariable=entradaNombre).place (x=70,y=20)
#creamos boton
botonOK = Button (emergente,text="OK",command=ok).place (x=100,y=50)
emergente.mainloop()   















class Riemann ():
    def crearPolinomio (self,linea_polinomio):
        # metemos los elementos del polinomio en una lista
        polinomio = linea_polinomio.split()
        # y la invertimos para que coincida su grado con el índice de la lista
        polinomio = list(reversed(polinomio))
        return polinomio
    
    def calculoFuncion (self,i,n_rectangulos,polinomio):
        valor = i * 1/int(n_rectangulos)
        acumulador = 0
        for j in range (len(polinomio)):
            acumulador = acumulador + (float(polinomio[j])*pow(valor,j))
        return acumulador

    def areaRiemann (self,n_rectangulos,polinomio):
        sumatorio = 0
        for i in range (int(n_rectangulos)):
            funcion = self.calculoFuncion (i,n_rectangulos,polinomio)
            # if funcion >0 and funcion < 1:
            sumatorio = sumatorio + ((1 / int(n_rectangulos)) * funcion)
        return round(sumatorio,5) 
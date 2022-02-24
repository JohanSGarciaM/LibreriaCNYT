from math import atan
from Convertir import *

def Fase(numero):
    numero = Convertir(numero)
    print(numero)

    #resultado es el arcotangente del numero imaginario sobre el numero real
    resultado = atan((numero[1]/numero[0]))
    resultado = float("%.2f" % resultado)
    #Retorna un numero flotante
    return resultado
    

    

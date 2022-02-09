from Convertir import *
from Conjugado import *
from producto import *

def Division(numero1,numero2):
    conjugado = Conjugado(numero2)
    numerador = Producto(numero1,conjugado)
    denominador = Producto(numero2,conjugado)
    numerador = Convertir(numerador)
    numerador[0]= float("%.2f" % (numerador[0]/int(denominador)))
    numerador[1]= float("%.2f" % (numerador[1]/int(denominador)))
    return(ConvertirC(numerador))

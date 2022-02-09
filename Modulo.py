from Convertir import *


def Modulo(numero):
    numero = Convertir(numero)
    resultado = (numero[0]**2)+((numero[1]**2))
    resultado = float("%.2f" % resultado**0.5)
    return resultado

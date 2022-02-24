from Convertir import *

def Conjugado(numero):
    numero = Convertir(numero)
    nuevo = [numero[0],numero[1]*-1]
    return(ConvertirC(nuevo))

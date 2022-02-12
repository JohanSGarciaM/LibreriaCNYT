from Convertir import *
from producto import *

def EscalarVector(escalar,vector):
    resultado = []
    escalar = str(escalar)
    for i in vector:
        resultado += [Producto(escalar,i)]
    return(resultado)


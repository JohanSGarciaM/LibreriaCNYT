from Convertir import *
from InversoAditivo import *

def InversoAditivoMatriz(matriz):
    for i in range(len(matriz)):
        matriz[i] = InversoAditivo(matriz[i])
    return(matriz)

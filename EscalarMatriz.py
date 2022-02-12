from EscalarVector import *

def EscalarMatriz(escalar,matriz):
    escalar = str(escalar)
    for i in range(len(matriz)):
        matriz[i]= EscalarVector(escalar,matriz[i])

    return matriz

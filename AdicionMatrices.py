from Convertir import *
from suma import *

def AdicionMatrices(matriz,matriz1):
    matrizNueva=[[0 for i in range(len(matriz[0]))]for j in range(len(matriz))]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matrizNueva[i][j]=suma(matriz[i][j],matriz1[i][j])
    return matrizNueva
            

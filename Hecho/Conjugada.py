from Conjugado import *

def ConjugadaVector(vector):
    for i in range(len(vector)):
        vector[i] = Conjugado(vector[i])
    return vector

def ConjugadaMatriz(matriz):
    for i in range(len(matriz)):
        matriz[i] = ConjugadaVector(matriz[i])

    return matriz

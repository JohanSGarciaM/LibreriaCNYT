from Convertir import *
from suma import suma

def AdicionVectores(vector1,vector2):
    resultado = []
    for i in range(len(vector1)):
        resultado+= [suma(vector1[i],vector2[i])]
    return(resultado)

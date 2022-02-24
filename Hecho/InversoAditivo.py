from Convertir import *

def InversoAditivo(vector):
    resultado=[]
    for i in vector:
        numero = Convertir(i)
        numero[0]*=-1
        numero[1]*=-1
        numero = ConvertirC(numero)
        resultado+=[numero]
    return(resultado)
        

from Convertir import *

def Producto(numero1,numero2):
    numero1 = Convertir(numero1)
    numero2 = Convertir(numero2)
    real = 0
    imaginario = 0
    real += numero1[0]*numero2[0]
    imaginario += numero1[0]*numero2[1]
    real += (numero1[1]*numero2[1])*-1
    imaginario += numero1[1]*numero2[0]
    return (ConvertirC([real,imaginario]))
        
            
            

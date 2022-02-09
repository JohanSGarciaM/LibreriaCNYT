from Convertir import *

def suma(num1,num2):
    num1 = Convertir(num1)
    num2 = Convertir(num2)
    real = num1[0] + num2[0]
    imaginario = num1[1] + num2[1]
    resultado = ConvertirC([real,imaginario])
    return resultado
    

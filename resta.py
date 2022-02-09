from Convertir import *

def resta(num1,num2):
    num1 =  Convertir(num1)
    num2 = Convertir(num2)
    nuevo = [num1[0]-num2[0],num1[1]-num2[1]]
    resultado = ConvertirC(nuevo)
    return resultado

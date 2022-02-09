from Convertir import Convertir,ConvertirC

def Producto(numero1,numero2):
    print(numero1,numero2)
    numero1=Convertir(numero1)
    numero2=Convertir(numero2)
    imaginaria = 0
    entero = 0
    print(numero1)
    print(numero2)
    entero = entero + numero1[0]*numero2[0]
    entero = entero + numero1[1]*numero2[1]*-1
    imaginaria = imaginaria + numero1[0]*numero2[1]
    imaginaria = imaginaria + numero1[1]*numero2[0]
    return ConvertirC([entero,imaginaria])
        
        
            
            

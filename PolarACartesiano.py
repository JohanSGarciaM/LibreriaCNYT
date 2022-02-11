from math import *
from Convertir import *

#La función recibe un real llamado numero y recibe un flotante llamado angulo

def PolarACartesiano(numero,angulo):
    x = radians(angulo)
    real = float("%.2f" % (numero*cos(x)))
    imaginario = float("%.2f" % (numero*sin(x)))
    resultado = [real,imaginario]
    return(ConvertirC(resultado))
    

from Fase import *
from Modulo import *

def CartesianoAPolar(numero):
    #Magnitud en tipo flotante
    magnitud = Modulo(numero)
    #Fase del numero 
    fase = Fase(numero)
    resultado = (magnitud,fase)
    return resultado
    

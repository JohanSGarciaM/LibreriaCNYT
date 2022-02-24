from math import *


"""Librería de Complejos

Autor : Johan Sebastian Garcia Martinez

Aclaraciones :

Los numeros imaginarios deben ingresar como un string y las funciones Convertir y ConvertirC manejarán los formatos

Los numeros reales deben ingresar como numero entero o flotante normal

"""

#Función que maneja los numeros que entran como string

def Convertir(numero):
    numero = numero.replace(" ","")
    negativos = 0
    positivos = 0
    for i in numero:
        if i=="-":negativos+=1
        if i=="+": positivos+=1
    #Solo enteros
    if numero[-1]!="i":return[int(numero),0]

    #Solo imaginarios negativos
    if (numero[-1]=="i" and positivos==0 and "-" in numero and numero.split("-")[0]=='' and len(numero.split("-"))<3) or (numero[-1]=="i" and positivos==0 and "-" not in numero):
        return [0,int(numero[:-1])]



    #Positivo positivo

    if negativos==0 and positivos==1 and numero[-1]=="i":
        numero=numero.split("+")
        return([int(numero[0]),int(numero[1][:-1])])


    #Positivo negativo

    if negativos==1 and positivos==0 and numero[0]!="-" and numero[-1]=="i":
        numero=numero.split("-")
        return([int(numero[0]),int(numero[1][:-1])*-1])

    #Negativo Positivo
    if negativos==1 and positivos==1 and numero[0]=="-" and numero[-1]=="i":
        numero=numero.split("+")
        return([int(numero[0]),int(numero[1][:-1])])

    #Negativo Negativo

    if negativos==2:
        numero=numero[1:].split("-")
        return([int(numero[0])*-1,int(numero[1][:-1])*-1])
 
#Funcion que recibe como parámetro un numero complejo en una lista y retorna el string correspondiente
    
def ConvertirC(complejo):
    if complejo[0] != 0:
        if complejo[1] >0:
            return (str(complejo[0])+"+"+str(complejo[1])+"i")
        elif complejo[1]==0:
            return(str(complejo[0]))
        else:
            return(str(complejo[0])+str(complejo[1])+"i")
    else:
        if complejo[1] >0:
            return (str(complejo[1])+"i")
        elif complejo[1]==0:
            return(str(complejo[0]))
        else:
            return(str(complejo[1])+"i")
            
#Función que recibe dos matrices y retorna la suma de ambas

def AdicionMatrices(matriz,matriz1):
    matrizNueva=[[0 for i in range(len(matriz[0]))]for j in range(len(matriz))]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matrizNueva[i][j]=suma(matriz[i][j],matriz1[i][j])
    return matrizNueva
            

#Función que recibe dos vectores y retorna la suma de ambos

def AdicionVectores(vector1,vector2):
    resultado = []
    for i in range(len(vector1)):
        resultado+= [suma(vector1[i],vector2[i])]
    return(resultado)


#Función que recibe un numero complejo en forma cartesiana y retorna su correspondiente en polar

def CartesianoAPolar(numero):
    #Magnitud en tipo flotante
    magnitud = Modulo(numero)
    #Fase del numero 
    fase = Fase(numero)
    resultado = (magnitud,fase)
    return resultado
    

#Función que recibe un vector y retorna su conjugado

def ConjugadaVector(vector):
    for i in range(len(vector)):
        vector[i] = Conjugado(vector[i])
    return vector

#Función que recibe una matriz y retorna su conjugada

def ConjugadaMatriz(matriz):
    for i in range(len(matriz)):
        matriz[i] = ConjugadaVector(matriz[i])

    return matriz


#Función que recibe un numero complejoy retorna su conjugado

def Conjugado(numero):
    numero = Convertir(numero)
    nuevo = [numero[0],numero[1]*-1]
    return(ConvertirC(nuevo))


#Función que recibe dos numeros complejos y retorna su división

def Division(numero1,numero2):
    conjugado = Conjugado(numero2)
    numerador = Producto(numero1,conjugado)
    denominador = Producto(numero2,conjugado)
    numerador = Convertir(numerador)
    numerador[0]= float("%.2f" % (numerador[0]/int(denominador)))
    numerador[1]= float("%.2f" % (numerador[1]/int(denominador)))
    return(ConvertirC(numerador))


#Función que recibe un escalar y una matriz, luego retorna su producto

def EscalarMatriz(escalar,matriz):
    escalar = str(escalar)
    for i in range(len(matriz)):
        matriz[i]= EscalarVector(escalar,matriz[i])

    return matriz


#Función que recibe un escalar y un vector, luego retorna su producto

def EscalarVector(escalar,vector):
    resultado = []
    escalar = str(escalar)
    for i in vector:
        resultado += [Producto(escalar,i)]
    return(resultado)


#Función que retorna un numero complejo y retorna su fase

def Fase(numero):
    numero = Convertir(numero)
    #resultado es el arcotangente del numero imaginario sobre el numero real
    resultado = atan((numero[1]/numero[0]))
    resultado = float("%.2f" % resultado)
    #Retorna un numero flotante
    return resultado


#Función que recibe un vector y retorna su inverso aditivo    

def InversoAditivo(vector):
    resultado=[]
    for i in vector:
        numero = Convertir(i)
        numero[0]*=-1
        numero[1]*=-1
        numero = ConvertirC(numero)
        resultado+=[numero]
    return(resultado)
        


#Función que recibe una matriz y retorna su inverso aditivo

def InversoAditivoMatriz(matriz):
    for i in range(len(matriz)):
        matriz[i] = InversoAditivo(matriz[i])
    return(matriz)


#Función que recibe un numero complejo y retorna su módulo

def Modulo(numero):
    numero = Convertir(numero)
    resultado = (numero[0]**2)+((numero[1])**2)
    
    resultado = float("%.2f" % resultado**0.5)
    return resultado


#Función que recibe los componentes de un numero polar y retorna la representación cartesiana

def PolarACartesiano(numero,angulo):
    x = radians(angulo)
    real = float("%.2f" % (numero*cos(x)))
    imaginario = float("%.2f" % (numero*sin(x)))
    resultado = [real,imaginario]
    return(ConvertirC(resultado))


#Función que recibe dos numeros complejos y retorna su producto

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
        

#Función que recibe dos numeros complejos y retorna su resta

def resta(num1,num2):
    num1 =  Convertir(num1)
    num2 = Convertir(num2)
    nuevo = [num1[0]-num2[0],num1[1]-num2[1]]
    resultado = ConvertirC(nuevo)
    return resultado


#Función que recibe dos numeros complejos y retorna su suma

def suma(num1,num2):
    num1 = Convertir(num1)
    num2 = Convertir(num2)
    real = num1[0] + num2[0]
    imaginario = num1[1] + num2[1]
    resultado = ConvertirC([real,imaginario])
    return resultado


#Función que recibe una matriz y retorna su transpuesta

def TranspuestaMatriz(matriz):
    trans = []
    for i in range(len(matriz[0])):
        trans.append([])
        for j in range(len(matriz)):
            trans[i].append(matriz[j][i])
    return trans


#Función que recibe un vector y retorna su transpuesta

def TranspuestaVector(vector):
    trans =[]
    for i in range(len(vector)):
        trans.append([])
        trans[i].append(vector[i])
    return trans


#Función que recibe un vector y retorna su daga

def DagaVector(vector):
    daga = ConjugadaVector(vector)
    daga = TranspuestaVector(daga)
    return daga
    

#Función que recibe una matriz y retorna su daga

def DagaMatriz(matriz):
    trans = []
    for i in range(len(matriz[0])):
        trans.append([])
        for j in range(len(matriz)):
            trans[i].append(Conjugado(matriz[j][i]))
    return trans


#Función que recibe dos matrices y las multiplica


def ProductoMatrices(matriz1,matriz2):
    nueva = []
    for i in range(len(matriz1)):
        nueva.append([])
        for j in range(len(matriz2[0])):
            nueva[i].append("0+0i")    
    for i in range(len(matriz1)):
        for j in range(len(matriz2[0])):
            for k in range(len(matriz1[0])):
                nueva[i][j] = suma(nueva[i][j],Producto(matriz1[i][k],matriz2[k][j]))
    return nueva

        


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
            


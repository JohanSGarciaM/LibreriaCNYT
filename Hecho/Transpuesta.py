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
        

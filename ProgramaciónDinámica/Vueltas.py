import math

#Naive aproach 
def coinChangeNaive(P, C):
    return coinChangeNaive_Aux(P, len(P) - 1, C)
#End def

def coinChangeNaive_Aux(P, i, C):
    #Si solo tengo monedas de 1, la cantidad sería el valor en esas monedas
    #Es decir, la cantidad de monedas es el valor mismo
    if P[i] == 1:
        return C
    #Si mi moneda actual es mayor, debo probar con una de menor denominación
    elif P[i] > C:
        return coinChangeNaive_Aux(P, i - 1, C)
    #Si no es mayor, puede ser menor o igual
    else:
        sinI = coinChangeNaive_Aux(P, i - 1, C)
        conI = coinChangeNaive_Aux(P, i, C - P[i]) + 1
        #Compruebo si es mejor utilizar la denominación actual, o no
        if sinI < conI:
            return sinI
        else:
            return conI
        #End if 
    #End if
#End def

#--------------------------------------------------------------

#Memoizacion
def coinChangeMemo(P, C):
    #Dos factores determinan el avance del algoritmo
    #La denominación y el valor restante por calcular
    M = [[math.inf for j in range (C + 1)] for i in range(len(P))]
    return coinChangeMemo_Aux(P, len(P) - 1, C, M)
#End def

def coinChangeMemo_Aux(P, i, C, M):
    #Ya calculé el cambio mínimo para el valor y la denominación?
    if M[i][C] == math.inf:
        #Si solo tengo monedas de 1, la cantidad sería el valor en esas monedas
        #Es decir, la cantidad de monedas es el valor mismo
        if P[i] == 1:
            M[i][C] = C
        #Si mi moneda actual es mayor, debo probar con una de menor denominación
        elif P[i] > C:
            M[i][C] = coinChangeMemo_Aux(P,i - 1, C, M)
        #Si no es mayor, puede ser menor o igual
        else:
            sinI = coinChangeMemo_Aux(P, i - 1, C, M)
            conI = coinChangeMemo_Aux(P, i, C - P[i], M) + 1
            #Compruebo si es mejor utilizar la denominación actual, o no
            if sinI < conI:
                M[i][C] = sinI
            else:
                M[i][C] = conI
            #End if 
        #End if
    #End if
    return M[i][C]
#End def

#--------------------------------------------------------------

#Bottom-up
def coinChangeBottom(P, C):
    sizeP = len(P)
    M = [[math.inf for j in range (C + 1)] for i in range(sizeP)]
    for v in range(C + 1):
        for i in range (sizeP):
            #Si solo tengo monedas de 1, la cantidad sería el valor en esas monedas
            #Es decir, la cantidad de monedas es el valor mismo
            if P[i] == 1:
                M[i][v] = v
            #Si mi moneda actual es mayor, debo probar con una de menor denominación
            elif P[i] > v:
                M[i][v] = M[i - 1][v]
            #Si no es mayor, puede ser menor o igual
            else:
                sinI = M[i - 1][v]
                conI = M[i][v - P[i]] + 1
                #Compruebo si es mejor utilizar la denominación actual, o no
                if sinI < conI:
                    M[i][v] = sinI
                else:
                    M[i][v] = conI
                #End if 
            #End if
        #End for
    #End for
    return M[sizeP - 1][C]
#End def

#--------------------------------------------------------------

 
P = [1, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000, 100000] 
C = 2511
#print(f"Según el algoritmo Naive, lo mínimo es {coinChangeNaive(P,C)}") 
print(f"Según el algoritmo con Memoizacion, lo mínimo es {coinChangeMemo(P,C)}") 
print(f"Según el algoritmo Bottom-up, lo mínimo es {coinChangeBottom(P,C)}")



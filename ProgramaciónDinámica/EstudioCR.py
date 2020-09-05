import math
#Maximización de la ganancia en el corte de tubos
#Implementación de la solución recursiva con algoritmo inocente recursivo 
def CutRodeNaive(size, Precios):
    #Caso Base 
    if size == 0:
        return 0
    else:
        #Teniendo en cuenta la solución recurrente: r(n) = max(pk + r(n-k))
        #Se pretende establecer un punto de comparación para encontrar el máximo
        q = -math.inf
        for k in range(1, size + 1):
            #Encuentro la ganancia para cada tamaño de corte
            profit = Precios[k - 1] + CutRodeNaive(size - k, Precios)
            #Guardo la más grande
            if q < profit:
                q = profit
            #End if
        #End for
        return q
    #End if
#End def

#Memoización del algoritmo utilizando una tabla llena de resultados calculados
def CutRodeMemo(size, Precios):
    #Inicializo la tabla de resultados
    M = [-math.inf]*(size+1)
    return CutRodeMemoAux(M, size, Precios)
#End def
#Se cambian los retornos para almacenar los resultados obtenidos 
def CutRodeMemoAux(M, size, Precios):
    #La solución ya está calculada?
    #Siempre se utiliza el atributo que controla la evolución del algoritmo
    #En este casp es size
    if M[size] == -math.inf:
        if size == 0:
            M[size] =  0
        else:
            #Teniendo en cuenta la solución recurrente: r(n) = max(pk + r(n-k))
            #Se pretende establecer un punto de comparación para encontrar el máximo
            q = -math.inf
            for k in range(1, size + 1):
                #Encuentro la ganancia para cada tamaño de corte
                profit = Precios[k - 1] + CutRodeMemoAux(M,size - k, Precios)
                #Guardo la más grande
                if q < profit:
                    q = profit
                #End if
            #End for
            M[size] = q
        #End if
    #End if
    return M[size]
#End def


#Transformar llamados recursivos en secuenciales
def CutRodeBottom(size, Precios):
    #Inicializo la tabla de resultados
    M = [0]*(size+1)
    #Caso Base
    M[0] = 0
    #Calcular el máximo para todos los tamaños hasta el solicitado
    #M[size] = [M0, M1, ...., MSize]
    for i in range (1, size+1):
        q = -math.inf
        for k in range(i):
            #Encuentro la ganancia para cada tamaño de corte
            profit = Precios[k] + M[i - k - 1]
            #Guardo la más grande
            if q < profit:
                q = profit
            #End if
        #End for
        M[i] = q
    #End for
    return M[size]
#End def

#Utilizar backtracking para encontrar los cortes que se deben hacer
def CutRodeBottomBackT(size, Precios):
    #Inicializo la tabla de resultados
    M = [-math.inf]*(size+1)
    #Para el BackTracking se emplea una segunda tabla
    BT = [-1]*(size+1)
    #Caso Base
    M[0] = 0
    #Calcular el máximo para todos los tamaños hasta el solicitado
    #M[size] = [M0, M1, ...., MSize]
    for i in range (1, size+1):
        for k in range(1, i +1):
            #Encuentro la ganancia para cada tamaño de corte
            profit = Precios[k - 1] + M[i - k]
            #Guardo la más grande
            if M[i] < profit:
                #Indice para valor máximo
                BT[i] = k
                #Valor máximo
                M[i] = profit
            #End if
        #End for
    #End for
    #La tabla de BackTracking me dice cómo debo cortar
    #Supongamos que T tiene los cortes que se deben realizar
    T = []
    #m representa el tamaño restante de la cuerda
    #Cuando no he realizado cortes, es igual al tamaño total
    m = size
    #Mientras que quede cuerda
    while m > 0:
        #BT indica el tamaño de los cortes
        #Guardo el corte óptimo para el tamaño actual de la cuerda (m)
        T.append(BT[m])
        #Reduzco el tamaño después de cortar
        m = m - BT[m]
    #End while
    return [M[size], T]
#End def


Precios1 = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
size = 10
print(f'Según el algoritmo naive')
print(f'Con la lista de precios {Precios1}, se obtiene un máximo de {CutRodeNaive(size, Precios1)}')
print(f'Según el algoritmo memoizado')
print(f'Con la lista de precios {Precios1}, se obtiene un máximo de {CutRodeMemo(size, Precios1)}')
print(f'Según el algoritmo Bottom-up')
print(f'Con la lista de precios {Precios1}, se obtiene un máximo de {CutRodeBottom(size, Precios1)}')
print(f'Según el algoritmo Bottom-up con backtracking')
print(f'Con la lista de precios {Precios1}:')
print(f'Se obtiene {CutRodeBottomBackT(size, Precios1)}')
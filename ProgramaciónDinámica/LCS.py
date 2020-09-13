import math
#Algoritmo Naive
def LCS(X, Y):
    #Se inicia de atrás hacia adelante
    return LCS_Aux(X, Y, len(X), len(Y))
#End def
def LCS_Aux(X, Y, i, j):
    if i == 0 or j == 0:
        return 0
    else:
        if X[i - 1] == Y[j - 1]:
            #c[i-1,j-1]+1
            return LCS_Aux(X, Y, i-1, j - 1) + 1
        else:
            #Decidir si resto a x o a y
            #Max(c[i,j-1],c[i-1,j])
            a = LCS_Aux(X, Y, i, j-1)
            b = LCS_Aux(X, Y, i - 1, j)
            if b < a:
                return a
            else:
                return b
            #End if
        #End if
    #End if
#End def

#Memoizacion
#Cambio todos los retornos por cambios en la tabla de soluciones
#Antes de calcular unasolución, verifico que no esté solucionada
def LCSMem(X, Y):
    #Creo la tabla de soluciones para revisar y evitar las busquedas de soluciones ya encontradas
    M = [ [ -math.inf for j in range(len(Y) + 1) ] for i in range (len(X) + 1)]
    return LCSMem_Aux(X, Y, len(X), len(Y), M)
#End def
def LCSMem_Aux(X, Y, i, j,M):
    #Verifico si ya he encontrado la solución
    if M[i][j] ==  -math.inf:
        if i == 0 or j == 0:
            M[i][j] = 0
        else:
            if X[i - 1] == Y[j - 1]:
                #c[i-1,j-1]+1
                M[i][j] =  LCSMem_Aux(X, Y, i-1, j - 1, M) + 1
            else:
                #Decidir si resto a x o a y
                #Max(c[i,j-1],c[i-1,j])
                a = LCSMem_Aux(X, Y, i, j-1, M)
                b = LCSMem_Aux(X, Y, i - 1, j, M)
                if b < a:
                    M[i][j] = a
                else:
                    M[i][j] = b
                #End if
            #End if
        #End if
    #End if 
    return M[i][j]
#End def

#Bottom-Up 
#Transformo la recurrencia en un problema secuencial
#Cambio todos los llamados recursivos por búsquedas en la tabla de soluciones
def LCSBottom(X, Y):
    #Creo la tabla de soluciones para revisar y evitar las busquedas de soluciones ya encontradas
    M = [ [ 0 for j in range(len(Y) + 1) ] for i in range (len(X) + 1)]
    for i in range (1, len(X) +1):
        for j in range(1, len(Y) +1):
            if X[i - 1] == Y[j - 1]:
                #c[i-1,j-1]+1
                M[i][j] =  M[i-1][j - 1] + 1
            else:
                #Decidir si resto a x o a y
                #Max(c[i,j-1],c[i-1,j])
                a = M[i][j-1]
                b = M[i-1][j]
                if b < a:
                    M[i][j] = a
                else:
                    M[i][j] = b
                #End if
            #End if
        #End for 
    #End for
    return M[i][j]
#End def

#Bottom-Up con BackTracking
def LCSBottomBack(X, Y):
    sizeX = len(X)
    sizeY = len(Y)
    #Creo la tabla de soluciones para revisar y evitar las busquedas de soluciones ya encontradas
    M = [ [ 0 for j in range(sizeY + 1) ] for i in range (sizeX + 1)]
    #Se crea un a tabla adicional para almacenar lo que me lleva a la solución
    BT = [ [ 0 for j in range(sizeY + 1) ] for i in range (sizeX + 1)]
    #Debo identificar que datos deben estar listos para avanzar
    for i in range (1, sizeX +1):
        for j in range(1, sizeY +1):
            if X[i - 1] == Y[j - 1]:
                #c[i-1,j-1]+1
                M[i][j] =  M[i-1][j - 1] + 1
                #Lo que me ayudó a ganar es restar en las dos cadenas
                BT[i][j] = [-1, -1]
            else:
                #Decidir si resto a x o a y
                #Max(c[i,j-1],c[i-1,j])
                a = M[i][j-1]
                b = M[i-1][j]
                if b < a:
                    M[i][j] = a
                    #Lo que me ayudó a ganar es restar en Y
                    BT[i][j] = [0, -1]
                else:
                    M[i][j] = b
                    #Lo que me ayudó a ganar es restar en X
                    BT[i][j] = [-1, 0]
                #End if
            #End if
        #End for 
    #End for
    Z = []
    [ i, j ] = [ sizeX, sizeY ]
    while i != 0 and j != 0:
        if BT[ i ][ j ][ 0 ] == BT[ i ][ j ][ 1 ]:
            Z = [ X[ i - 1 ] ] + Z
        #End if
        [ i, j ] = [ i + BT[ i ][ j ][ 0 ], j + BT[ i ][ j ][ 1 ] ]
    #End while
    return [M[sizeX][sizeY],Z]
#End def

X = "dabale arroz a la zorra el adab"
Y = "anita lava la tina"
##print(f'La máxima cadena matricial tiene una longitud de {LCS(X, Y)} según el algoritmo Naive')
print(f'La secuencia común más larga mide {LCSMem(X, Y)} según el algoritmo Memoizado')
print(f'La secuencia común más larga mide {LCSBottom(X, Y)} según el algoritmo Bottom-Up')
print(f'secuencia común más larga es {LCSBottomBack(X, Y)} según el algoritmo Bottom-Up con BackTracking')


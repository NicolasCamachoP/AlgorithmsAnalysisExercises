import math
#Impresión de tabla
def PrintMatrix(M):
    for j in range (len(M)):
        for i in range(len(M)):
            if M[i][j] == math.inf:
                print(".", end = "")
            else:
                print("x", end = "")
            #End if
        #End for  
        print('')
    #End for
    print('-------------------')

#Algoritmo inocente recursivo
def MatrixMult(D):
    return MatrixMult_Aux(D, 1, len(D) - 1)
#End def

def MatrixMult_Aux (D, i, j):
    #Caso Base: El número óptimo de multiplicaciones escalares agrupando una matríz con ella misma 
    if i == j:
        return 0
    else:
    #Se pretende encontrar Mij (número óptimo de multiplicaciones escalares al agrupar las matrices Ai-Aj)
    #Mi,j = min(Mi,k + Mk+1,j + mikj)
        q = math.inf
        for k in range(i, j):
            #Mi,k
            left = MatrixMult_Aux(D, i, k)
            #Mk+1,j
            right = MatrixMult_Aux(D, k+1, j)
            #mikj = rickcj = Di-1DkDj
            mikj = D[i-1]*D[k]*D[j]
            m = left + right + mikj
            #Se necesita el mínimo
            if q > m:
                q = m
            #End if
        #End for
        return q
    #End if
#End def


#Memoización 
#Se pretende encontrar soluciones ya encontradas, de modo que se deben almacenar en algún lugar
def MatrixMultMem(D):
    M = [ [ math.inf for i in range(len(D)) ] for j in range (len(D))]
    return MatrixMultMem_Aux(D, 1, len(D) - 1, M)
#End def
def MatrixMultMem_Aux (D, i, j, M):
    #Se verifica que se haya encontrado la solución 
    if M[i][j] == math.inf:
        #Caso Base: El número óptimo de multiplicaciones escalares agrupando una matríz con ella misma 
        if i == j:
            M[i][j] = 0
        else:
        #Se pretende encontrar Mij (número óptimo de multiplicaciones escalares al agrupar las matrices Ai-Aj)
        #Mi,j = min(Mi,k + Mk+1,j + mikj)
            q = math.inf
            for k in range(i, j):
                #Mi,k
                left = MatrixMult_Aux(D, i, k)
                #Mk+1,j
                right = MatrixMult_Aux(D, k+1, j)
                #mikj = rickcj = Di-1DkDj
                mikj = D[i-1]*D[k]*D[j]
                m = left + right + mikj
                #Se necesita el mínimo
                if q > m:
                    q = m
                #End if
            #End for
            M[i][j] = q
        #End if
    #End if
    return M[i][j]
#End def


#Bottom-Up
#El algoritmo no va a ser recursivo al volverse se cuencial
def MatrixMultBottom(D):
    M = [ [ math.inf for i in range(len(D)) ] for j in range (len(D))]
    for j in range(len(M)):
        for i in range (j,0, -1):
            if (i == j):
                M[i][j] = 0
                #PrintMatrix(M)
            else:
                q = math.inf
                for k in range(i, j):
                    left = M[i][k]
                    right = M[k + 1][j]
                    m = left + right + ( D[i-1] * D[k] * D[j] )
                    if m < q:
                        q = m
                    #End if
                #End for
                M[i][j] = q
                #PrintMatrix(M)
            #End if
        #End for
    #End for
    return M[i][j]
#End def


#Bottom-up con Backtracking 
#Se pretende informar cómo se deben hacer las multiplicaciones, no solo el número óptimo
def MatrixMultBottomBack(D):
    M = [ [ math.inf for i in range(len(D)) ] for j in range (len(D))]
    #Se deben almacenar las agrupaciones que me permien llegar al número óptimo de multiplicaciones
    BT = [ [ 0 for i in range(len(D)) ] for j in range (len(D))]
    for j in range(len(M)):
        for i in range (j,0, -1):
            if (i == j):
                M[i][j] = 0
                #PrintMatrix(M)
            else:
                q = math.inf
                w = -1
                for k in range(i, j):
                    left = M[i][k]
                    right = M[k + 1][j]
                    m = left + right + ( D[i-1] * D[k] * D[j] )
                    if m < q:
                        q = m
                        #Se almacena el indice k que permitió encontrar el número óptimo
                        w = k
                    #End if
                #End for
                #Siempre que se modifica M se debe modificar BT
                M[i][j] = q
                #POsición donde se debe guardar el paréntesis
                BT[i][j] = w
                #PrintMatrix(M)
            #End if
        #End for
    #End for
    return [M[i][j], MatrixBacktracking(BT, i, j)]
#End def
#Para entender el Back tracking se debe tener en cuenta que la matriz de BackTracking indica en donde se pone pivote de paréntesis
#LA última posición ij indica donde se debe poner un paréntesis
#Al hacer esto se divide en dos grupos las matrices, (A1,Ak)(Ak+1,An)
#De modo que es un acercamiento a dividir a vencer puesto que se debe consultar la matriz para encontrar el próximo pivote de cada mitad
#El de la izquiera estaría en BT[1][k] y el de la derecha en BT[k+1][n]
def MatrixBacktracking(BT, i, j):
    if i == j:
        return "A_{:d}".format(i)
    else:
        left = MatrixBacktracking(BT, i , BT[i][j])
        right = MatrixBacktracking(BT, BT[i][j] + 1, j)
        return "(" + left +")(" + right + ")"


D = [10,100,5,50, 3, 2, 10, 125, 35, 246]
print(f"Mínimo número de multiplicaciones - Naive: {MatrixMult(D)}")
print(f"Mínimo número de multiplicaciones - Memoización: {MatrixMultMem(D)}")
print(f"Mínimo número de multiplicaciones - Bottom-Up: {MatrixMultBottom(D)}")
print(f"Mínimo número de multiplicaciones - Bottom-Up Backtracking: {MatrixMultBottomBack(D)}")
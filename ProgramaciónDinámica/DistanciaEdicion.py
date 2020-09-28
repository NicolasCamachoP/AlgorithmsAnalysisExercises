def PrintMatrix( M, x, y ):
  for j in range( x ):
    for i in range( y ):
        print(M[i][j], end = "")
    # end for
    print( "" )
  # end for
  print( "---------------------" )
# end def

#------------------------------------------------------------------------------------------------------

#Naive
def distENaive_Aux(word1, word2, i, j):
    #Si j es 0, la distancia es el tamaño restante por procesar de word1 (i)
    if j == 0:
        return i
    #Si n es 0, la distancia es el tamaño restante por procesar de word2 (m)
    elif i == 0:
        return j
    #Si el caracter es igual, debo continuar con el siguiente de atrás hacia adelante
    elif word1[i - 1] == word2[j - 1]:
        return distENaive_Aux(word1, word2, i - 1, j - 1)
    #Si difieren, tengo que encontrar la mejor operación para igualarlos (inserciones, borrados y cambios)
    else:
        #Si inserto, el tamaño de word2 aumenta (i-1, j)
        #Si borro, el tamaño de word2 disminuye (i, j-1)
        #Si cambio, el tamaño se mantiene y debo continuar con la siguiente letra(i-1, j-1)
        #Debo elegir el mejor camino y sumo 1 por el paso que acabo de realizar
        return min(distENaive_Aux(word1, word2, i-1, j), distENaive_Aux(word1, word2, i, j-1),
        distENaive_Aux(word1, word2, i-1, j-1)) + 1
    #End if
#End def 
def distENaive(word1, word2):
    return distENaive_Aux(word1, word2, len(word1), len(word2))
#End def

#------------------------------------------------------------------------------------------------------

#Memoización
def distEMem_Aux(word1, word2, i, j, M):
    if M[i][j] == -1:
        #Si j es 0, la distancia es el tamaño restante por procesar de word1 (i)
        if j == 0:
            M[i][j] = i
        #Si n es 0, la distancia es el tamaño restante por procesar de word2 (m)
        elif i == 0:
            M[i][j] = j
        #Si el caracter es igual, debo continuar con el siguiente de atrás hacia adelante
        elif word1[i - 1] == word2[j - 1]:
            M[i][j] = distEMem_Aux(word1, word2, i - 1, j - 1, M)
        #Si difieren, tengo que encontrar la mejor operación para igualarlos (inserciones, borrados y cambios)
        else:
            #Si inserto, el tamaño de word2 aumenta (i-1, j)
            #Si borro, el tamaño de word2 disminuye (i, j-1)
            #Si cambio, el tamaño se mantiene y debo continuar con la siguiente letra(i-1, j-1)
            #Debo elegir el mejor camino y sumo 1 por el paso que acabo de realizar
            M[i][j] = min(distEMem_Aux(word1, word2, i-1, j, M), distEMem_Aux(word1, word2, i, j-1, M),
            distEMem_Aux(word1, word2, i-1, j-1, M)) + 1
        #End if
    #End if
    #PrintMatrix(M)
    return M[i][j]
#End def
def distEMem(word1, word2):
    M = [ [ -1 for j in range(len(word2) + 1) ] for i in range (len(word1) + 1)]
    return distEMem_Aux(word1, word2, len(word1), len(word2), M)
#End def

#------------------------------------------------------------------------------------------------------

#Bottom-Up
def distEBottom(word1, word2):
    #Tamaños de las palabras
    n = len(word1)
    m = len(word2)
    #Tabla considerando un string vacío
    M = [[0 for x in range(m + 1)] for x in range(n + 1)] 
    for i in range (n + 1 ):
        for j in range(m + 1):
            #Si m es 0, la distancia es el tamaño restante por procesar de word1 (i)
            #Equivalente a j inserciones
            if i == 0:
                M[i][j] = j
            #Si n es 0, la distancia es el tamaño restante por procesar de word2 (j)
            #Equivalente a i borrados
            elif j == 0:
                M[i][j] = i
            #Si el caracter es igual, debo continuar con el siguiente de atrás hacia adelante
            elif word1[i - 1] == word2[j - 1]:
                M[i][j] = M[i-1][j-1]
            #Si difieren, tengo que encontrar la mejor operación para igualarlos (inserciones, borrados y cambios)
            else:
                #Si inserto, el tamaño de word2 aumenta (i-1, j)
                insTotal = M[i-1][j]
                #Si borro, el tamaño de word2 disminuye (i, j-1)
                borTotal = M[i][j-1]
                #Si cambio, el tamaño se mantiene y debo continuar con la siguiente letra(i-1, j-1)
                camTotal = M[i-1][j-1]
                #Debo elegir el mejor camino y sumo 1 por el paso que acabo de realizar
                if insTotal < borTotal:
                    if insTotal < camTotal:
                        #Debo insertar
                        M[i][j] = M[i-1][j] + 1
                    else:
                        #Debo cambiar
                        M[i][j] = M[i-1][j-1] + 1
                    #End if
                else:
                    if borTotal < camTotal:
                        #Debo borrar
                        M[i][j] = M[i][j-1] + 1
                    else:
                        #Debo cambiar
                        M[i][j] = M[i-1][j-1] + 1
                    #End if
                #End if
            #End if
        #End for
    #End for
    return M[n][m]
#End def

#------------------------------------------------------------------------------------------------------

#Bottom-Up con Backtracking
def distEBB(word1, word2):
    #Tamaños de las palabras
    n = len(word1)
    m = len(word2)
    #Tabla considerando un string vacío
    M = [[0 for x in range(m + 1)] for x in range(n + 1)] 
    BT = [[[0,0] for x in range(m + 1)] for x in range(n + 1)]

    for i in range ( n + 1):
        for j in range( m + 1):
            #Si m es 0, la distancia es el tamaño restante por procesar de word1 (i)
            #Equivalente a j inserciones
            if i == 0:
                M[i][j] = j
                BT[i][j] = [-1,0]
            #Si n es 0, la distancia es el tamaño restante por procesar de word2 (j)
            #Equivalente a i borrados
            elif j == 0:
                M[i][j] = i
                BT[i][j] = [0,-1]
            #Si el caracter es igual, debo continuar con el siguiente de atrás hacia adelante
            elif word1[i - 1] == word2[j - 1]:
                M[i][j] = M[i-1][j-1]
            #Si difieren, tengo que encontrar la mejor operación para igualarlos (inserciones, borrados y cambios)
            else:
                #Si inserto, el tamaño de word2 aumenta (i-1, j)
                insTotal = M[i-1][j]
                #Si borro, el tamaño de word2 disminuye (i, j-1)
                borTotal = M[i][j-1]
                #Si cambio, el tamaño se mantiene y debo continuar con la siguiente letra(i-1, j-1)
                camTotal = M[i-1][j-1]
                #Debo elegir el mejor camino y sumo 1 por el paso que acabo de realizar
                if insTotal < borTotal:
                    if insTotal < camTotal:
                        #Debo insertar
                        M[i][j] = M[i-1][j] + 1
                        BT[i][j] = [-1,0]
                    else:
                        #Debo cambiar
                        M[i][j] = M[i-1][j-1] + 1
                        BT[i][j] = [-1,-1]
                    #End if
                else:
                    if borTotal < camTotal:
                        #Debo borrar
                        M[i][j] = M[i][j-1] + 1
                        BT[i][j] = [0,-1]
                    else:
                        #Debo cambiar
                        M[i][j] = M[i-1][j-1] + 1
                        BT[i][j] = [-1,-1]
                    #End if
                #End if
            #End if
        #End for
    #End for
    #PrintMatrix(BT, n, m)
    #PrintMatrix(M, n, m)
    steps = []
    [ i, j ] = [ n, m ]
    while i > 0 and j > 0:
        if (BT[i][j] == [0,0]):
            i -= 1
            j -= 1
            continue
        elif (BT[i][j] == [-1,0]):
            steps.append(f'Insertar {word1[i - 1]}')
        elif (BT[i][j] == [0,-1]):
            steps.append(f'Borrar {word2[j-1]}')
        elif (BT[i][j] == [-1,-1]):
            steps.append(f'Cambiar {word2[j-1]} por {word1[i-1]}')
        #End if
        [ i, j ] = [ i + BT[i][j][0], j + BT[i][j][1]]
    #End while
    return [M[n][m],steps]
#End def

#------------------------------------------------------------------------------------------------------

word1 = "tigre"
word2 = "trigo"
#print(f'Según el algoritmo Naive, la distancia de edición entre {word1} y {word2} es de {distENaive(word1, word2)}!')
#print(f'Según el algoritmo Memoización, la distancia de edición entre {word1} y {word2} es de {distEMem(word1, word2)}!')
#print(f'Según el algoritmo Bottom-Up, la distancia de edición entre {word1} y {word2} es de {distEBottom(word1, word2)}!')
BBA = distEBB(word1, word2)
print(f'Según el algoritmo Bottom-Up con BackTracking, la distancia de edición entre {word1} y {word2} es de {BBA[0]}!')
print(f'Se requiere {BBA[1]}')
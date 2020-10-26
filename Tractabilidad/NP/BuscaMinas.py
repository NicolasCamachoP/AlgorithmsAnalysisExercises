import random, sys, math

neighbors = [(1, 0), (1, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, 1)]
markedMines = set()


def boardGenerator(nRows, nCols, nMines):
    coordsMines = minesCoordList(nMines, nRows, nCols)
    Board = [[0 for j in range(nCols)] for i in range(nRows)]
    for element in coordsMines:
        Board[element[0]][element[1]] = -1
    #End for
    for i in range(nRows):
        for j in range(nCols):
            Board[i][j] = countMines(Board, i, j, nRows, nCols)
        #End for
    #End for
    return Board
#End def

# ------------------------------------------------------------------------

def minesCoordList(nMines, nRows, nCols):
    coordsMines = set()
    while len(coordsMines) < nMines:
        coordsMines.add((random.randint(0, nRows - 1),random.randint(0, nCols - 1)))
    #End while
    return coordsMines
#End def

# ------------------------------------------------------------------------

def countMines(M, i, j, nRows, nCols):
    if M[i][j] != -1:
        total = 0
        for neighbor in neighbors:
            point = [i + neighbor[0], j + neighbor[1]]
            if (point[0] < 0 or point[1] < 0 or point[0] > nRows - 1 or point[1] > nCols - 1):
                continue
            elif M[point[0]][point[1]] == -1:
                total += 1
            #End if
        #End for
        return total
    else:
        return -1
    #End if
#End def

# ------------------------------------------------------------------------

def printMatrix(M):
    print("---------------------------------------")
    for i in M:
        for j in i:
            if j == -1:
                print("x", end = "   ")
            else:
                print(j, end = "   ")
            #End if
        #End for
        print()
    #End for
    print("---------------------------------------")
#End def

def printMatrixProb(M):
    print("---------------------------------------")
    for i in M:
        for j in i:
            print('{:6f}'.format(j), end = "")
        #End for
        print()
    #End for
    print("---------------------------------------")
#End def

# ------------------------------------------------------------------------

def isNextToBorder(isClicked, i, j, nRows, nCols):
    for neighbor in neighbors:
        point = [i + neighbor[0], j + neighbor[1]]
        if (point[0] < 0 or point[1] < 0 or point[0] > nRows - 1 or point[1] > nCols - 1):
            continue
        elif Board[point[0]][point[1]] != -1 and isClicked[point[0]][point[1]]:
            return True
        #End if
    #End for
    return False
#End def

# ------------------------------------------------------------------------

def getNeighborsUnClicked(isClicked, i, j, nRows, nCols):
    nNeighbors = 0
    for neighbor in neighbors:
        point = [i + neighbor[0], j + neighbor[1]]
        if (point[0] < 0 or point[1] < 0 or point[0] > nRows - 1 or point[1] > nCols - 1):
            continue
        elif not isClicked[point[0]][point[1]]:
            nNeighbors += 1
        #End if
    #End for
    return nNeighbors
#End def

# ------------------------------------------------------------------------

def getBorderProb(isClicked, i, j, nRows, nCols, Board, defaultProb):
    prob = 0
    itChange = False
    for neighbor in neighbors:
        point = [i + neighbor[0], j + neighbor[1]]
        if (point[0] < 0 or point[1] < 0 or point[0] > nRows - 1 or point[1] > nCols - 1):
            continue
        elif Board[point[0]][point[1]] != -1 and isClicked[point[0]][point[1]]:
            #value of Neighbor divided by neighbors unclicked
            itChange = True
            prob += float(Board[point[0]][point[1]]
            /getNeighborsUnClicked(isClicked, point[0], point[1], 
            nRows, nCols))
        #End if
    #End for
    if itChange:
        return prob
    else:
        return defaultProb
#End def

# ------------------------------------------------------------------------

def updateProbability(probMatrix, isClicked, nMines, nUnclicked, nRows, nCols):
    #printMatrix(probMatrix)
    print("Actualizando matriz de probabilidad")
    prob = float(nMines/nUnclicked)
    for i in range(nRows):
        for j in range(nCols):
            if not isClicked[i][j]:
                if isNextToBorder(isClicked, i, j, nRows, nCols):
                    probMatrix[i][j] = round(getBorderProb(isClicked, i, j, nRows, 
                    nCols, Board, prob), 3)
                else:
                    probMatrix[i][j] = round(prob,3)
                #End if
            else:
                #Si ya le di click, la probabilidad es 0%
                probMatrix[i][j] = 0.000
            #End if
        #End for
    #End for
    #printMatrix(probMatrix)
    #printMatrix(isClicked)
    return probMatrix
#End def

# ------------------------------------------------------------------------

def getNextClick(probM, nRows, nCols, isClicked):
    print("Buscando siguiente click")
    point = [-1, -1]
    min = math.inf
    for i in range(nRows):
        for j in range(nCols):
            aux = probM[i][j]
            if aux < min and not isClicked[i][j]:
                min = aux
                point[0] = i
                point[1] = j
            #End if
        #End for
    #End for
    return point
#End def

# ------------------------------------------------------------------------

def recursiveClick(i, j, isClicked, Board, nRows, nCols):
    isClicked[i][j] = True
    for it in neighbors:
        point = [i + it[0], j + it[1]]
        if (point[0] < 0 or point[1] < 0 or point[0] > nRows - 1 or point[1] > nCols - 1):
            continue
        elif Board[point[0]][point[1]] == 0 and not isClicked[point[0]][point[1]]:
            recursiveClick(point[0], point[1], isClicked, Board, nRows, nCols)
        elif Board[point[0]][point[1]] != 0 and not isClicked[point[0]][point[1]]:
            isClicked[point[0]][point[1]] = True
        #End if
    #End for
    return isClicked
#End def

# ------------------------------------------------------------------------

def printRealBoard(isClicked, nRows, nCols, Board):
    marked = False
    for i in range(nRows):
        for j in range(nCols):
            if isClicked[i][j]:
                for it in markedMines:
                    if it[0] == i and it[0] == j:
                        marked = True 
                        break
                if marked:
                    print("M", end =" ")
                else:      
                    print(Board[i][j], end =" ")
                marked = False
            else:
                print("?", end = " ")    
            #End if
        #End for
        print()
    #End for
    print("--------------------------")
#End def

# ------------------------------------------------------------------------

def getUnclicked(isClicked):
    total = 0
    for i in isClicked:
        for j in i:
            if j:
                total += 1
            #End if
        #End if
    #End if
    return total
#End def 

# ------------------------------------------------------------------------

def buscaMinas_h0_Aux(Board, nRows, nCols, nMines, probM, isClicked, i, j, nUnclicked):
    print(f"Clickeando en {i + 1} {j + 1}")
    if Board[i][j] != -1:
        if Board[i][j] != 0:
            nUnclicked -= 1
            #Gana si ya clickeó todas sin perder
            if nUnclicked <= nMines:
                print("ya clickeó todas las que no son minas")
                printRealBoard(isClicked, nRows, nCols, Board)
                return True
            else: 
                isClicked[i][j] = True
                probM = updateProbability(probM, isClicked, nMines, nUnclicked, nRows, nCols)
                point = getNextClick(probM, nRows, nCols, isClicked)
                if point[0] != -1 and point[1] != -1:
                    return buscaMinas_h0_Aux(Board, nRows, nCols, nMines, probM, isClicked, 
                    point[0], point[1], nUnclicked)
                else:
                    print("********Falló la búsqueda del mínimo*********")
                    printRealBoard(isClicked, nRows, nCols, Board)
                    return False
                #End if
            #End if
        else:
            isClicked = recursiveClick(i,j, isClicked, Board, nRows, nCols)
            #printRealBoard(isClicked, nRows, nCols, Board)
            nUnclicked = getUnclicked(isClicked)
            probM = updateProbability(probM, isClicked, nMines, nUnclicked, nRows, nCols)
            #printMatrix(probM)
            point = getNextClick(probM, nRows, nCols, isClicked)
            if point[0] != -1 and point[1] != -1:
                return buscaMinas_h0_Aux(Board, nRows, nCols, nMines, probM, isClicked, 
                point[0], point[1], nUnclicked)
            else:
                print("********Falló la búsqueda del mínimo*********")
                printRealBoard(isClicked, nRows, nCols, Board)
                return False
            #End if
        #End if
    else:
        print(f"Clickeó una mina en {i + 1} {j + 1}")
        printRealBoard(isClicked, nRows, nCols, Board)
        return False
    #End if
#End def

# ------------------------------------------------------------------------

def buscaMinas_h0(Board, nRows, nCols, nMines):
    probMatrix = [[math.inf for j in range(nCols)] for i in range(nRows)]
    isClicked = [[False for j in range(nCols)]for i in range(nRows)]
    probMatrix = updateProbability(probMatrix, isClicked, nMines, nRows*nCols, nRows, nCols)
    return buscaMinas_h0_Aux(Board, nRows, nCols, nMines, probMatrix, isClicked,
    random.randint(0,nRows - 1), random.randint(0,nCols - 1), nRows*nCols)
#End def


## -------------------------------------------------------------------------
## -- Test

if len(sys.argv) == 4:
    if int(sys.argv[3]) <int(sys.argv[1])*int(sys.argv[2]):
        Board = boardGenerator(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
        printMatrix(Board)
        if buscaMinas_h0(Board, int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])):
            print("--------------------------------------------------------------------")
            print("Solución alcanzada con éxito")
            print("--------------------------------------------------------------------")
        else:
            print("--------------------------------------------------------------------")
            print("Pisó una mina")
            print("--------------------------------------------------------------------")
        #End if
    else:
        print("Número de minas demasiado grande")
    #End if
else:
    print("Argumentos erroneos")
    print("Debe ser: nRows nCols nMines")
#End if
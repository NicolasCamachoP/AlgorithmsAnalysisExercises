"""
A chef has collected data on the satisfaction level of his n dishes. 
Chef can cook any dish in 1 unit of time.

Like-time coefficient of a dish is defined as the time taken to cook 
that dish including previous dishes multiplied by its satisfaction level  
i.e. time[i]*satisfaction[i]

Return the maximum sum of Like-time coefficient that the chef can obtain after 
dishes preparation.

Dishes can be prepared in any order and the chef can discard some dishes 
to get this maximum value.

"""
import math
def printMatrix(M, lenx, leny):
    print("-------------------------------")
    for i in range(lenx):
        for j in range(leny):
            print(str(M[i][j]) + " ", end = "")
        #End for
        print()
    #End for
    print("-------------------------------")
#End def

#Naive
def LTC_Naive(SOriginal):
    S = SOriginal
    S.sort()
    return (LTC_NaiveAux(S, 0, 1))
#End def

def LTC_NaiveAux(S, i, j):
    if i >= len(S):
        return 0
    else:
        inSol = j*S[i] + LTC_NaiveAux(S, i + 1, j + 1)
        outSol = LTC_NaiveAux(S, i + 1, j)
        return max(inSol, outSol)
    #End if 
#End def

#Memoizado
def LTC_Mem(SOriginal):
    S = SOriginal
    S.sort()
    M = [[-math.inf for j in range(len(SOriginal))] for i in range(len(SOriginal))]
    return (LTC_MemAux(S, 0, 1, M))
#End def

def LTC_MemAux(S, i, j, M):
    if i >= len(S):
        return 0
    if M[i][j - 1] == -math.inf:
        inSol = j*S[i] + LTC_MemAux(S, i + 1, j + 1, M)
        outSol = LTC_MemAux(S, i + 1, j, M)
        M[i][j - 1] = max(inSol, outSol)
    return M[i][j - 1]
    #End if 
#End def

#Bottom-Up
def LTC_Bottom(SOriginal):
    M = [[0 for j in range(len(SOriginal) + 1)] for i in range(len(SOriginal) + 1)]
    S = SOriginal
    S.sort()
    for i in range(len(S) - 1, -1, -1):
        for j in range(1, len(S) + 1):
            inSol = (j)*S[i] + M[i + 1][j]
            outSol = M[i + 1][j - 1]
            M[i][j - 1] = max(inSol, outSol)
        #End for
    #End for
    return M[0][0]
#End def

#BackTracking MDF
def LTC_Back(SOriginal):
    M = [[0 for j in range(len(SOriginal) + 1)] for i in range(len(SOriginal) + 1)]
    BT = [[-math.inf for j in range(len(SOriginal) + 1)] for i in range(len(SOriginal) + 1)]
    S = SOriginal
    S.sort()
    for i in range(len(S) - 1, -1, -1):
        for j in range(1, len(S) + 1):
            inSol = (j)*S[i] + M[i + 1][j]
            outSol = M[i + 1][j - 1]
            if inSol > outSol:
                M[i][j - 1] = inSol
                BT[i][j - 1] = i   
            else:
                M[i][j - 1] = outSol
                BT[i][j - 1] = -math.inf
            #BT[i][j - 1] = ???
        #End for
    #End for
    #printMatrix(BT, len(S) +1 , len(S) +1 )
    R = []
    for i in range(len(S) + 1):
        if BT[i][i] != -math.inf:
            R.append(S[BT[i][i]])
        #End if
    #End for
    return [M[0][0],R]
#End def

Tests = []
Tests.append([-1, -8, 0, 5, -9])
Tests.append([4, 3, 2])
Tests.append([-1, -4, -5])
Tests.append([-2, 5, -1, 0, 3, -3])
for i in range(len(Tests)):
    print(f"Test {i + 1}")
    print(f"Naive algo max found {LTC_Naive(Tests[i])}")
    print(f"Memoizated algo max found {LTC_Mem(Tests[i])}") 
    print(f"Bottom-Up algo max found {LTC_Bottom(Tests[i])}")
    sol = LTC_Back(Tests[i])    
    print(f"Back algo max found {sol[0]}")
    print(f"Bottom-Up algo orders {sol[1]}")

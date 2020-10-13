import math
def removeMin(S):
    min = math.inf
    index = -1
    for i in range(len(S)):
        if S[i]<= min:
            index = i
            min = S[i]
        #End if
    #End for
    S.pop(index)
    return S
#End def

#Naive
def CGNaive(S):
    if len(S)%2 !=0:
        S = removeMin(S)
    #End if
    return CGNaive_Aux(S, 0, len(S) - 1)
#End def

def CGNaive_Aux(S, i, j):
    if i >= j:
        return 0
    else:
        a = CGNaive_Aux(S, i + 1, j - 1) + S[j]
        b = CGNaive_Aux(S, i, j - 2) + S[j]
        c = CGNaive_Aux(S, i + 1, j - 1) + S[i]
        d = CGNaive_Aux(S, i + 2, j) + S[i]
        return max(a, b, c, d)
    #End if
#End def

#Memoizado 
def CGMem(S):
    if len(S)%2 !=0:
        S = removeMin(S)
    #End if
    M = [[-math.inf for j in range(len(S) + 1)] for i in range(len(S) + 1)] 
    return CGMem_Aux(S, 0, len(S) - 1, M)
#End def

def CGMem_Aux(S, i, j, M):
    if M[i][j] == -math.inf:
        if i >= j:
            M[i][j] = 0
        else:
            a = CGMem_Aux(S, i + 1, j - 1, M) + S[j]
            b = CGMem_Aux(S, i, j - 2, M) + S[j]
            c = CGMem_Aux(S, i + 1, j - 1, M) + S[i]
            d = CGMem_Aux(S, i + 2, j, M) + S[i]
            M[i][j] = max(a, b, c, d)
        #End if
    #End if
    return M[i][j]
#End def

#Bottom-Up
def CGBottom(S):
    if len(S)%2 !=0:
        S = removeMin(S)
    #End if
    M = [[0 for j in range(len(S))] for i in range(len(S))] 
    for i in range(len(S) - 1, -1, -1):
        for j in range(0, len(S)):
            if i < j:
                if i + 1 < len(S) and 0 <= j - 1:
                    a = M[i + 1][j - 1] + S[j]
                    c = M[i + 1][j - 1] + S[i]
                else:
                    a = 0
                    c = 0
                if 0 <= j - 2:
                    b = M[i][j - 2] + S[j]
                else:
                    b = 0
                if i + 2 < len(S):
                    d = M[i + 2][j] + S[i]
                else:
                    d = 0
                M[i][j] = max(a, b, c, d)
            #End if
    #End for
    return M[0][len(S) - 1]
#End def
Test = []
Test.append([1000, 50, 50 , 200, 10])
Test.append([100, 500, 50, 1000, 100, 200, 50, 1000, 200, 50])
Test.append([100, 500, 50, 1000, 100, 200, 50, 1000, 200, 50, 1000])
Test.append([100, 500, 50, 1000, 100, 200, 100, 500, 500])
Test.append([ 50, 1000, 200, 50])
for test in Test:
    print(f"Naive: {CGNaive(test)}")
    print(f"Memoizado: {CGMem(test)}")
    print(F"Bottom: {CGBottom(test)}")
#End for
#Coger el mayor en cada iteración para greed


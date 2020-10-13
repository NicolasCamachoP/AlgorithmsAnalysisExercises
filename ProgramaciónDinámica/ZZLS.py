import math
#Naive aproach
def ZZLSNaiveWrap(S):
    p = ZZLSNaive_Aux(S, 0, 1)
    n = ZZLSNaive_Aux(S, 0, -1)
    if n < p:
        return p
    else: 
        return n 
    #End if
#End def 
def ZZLSNaive_Aux(S, i, k):
    if i < len(S):
        p = NextElement(S, i, k)
        a = ZZLSNaive_Aux(S, i + 1, k)
        b = 1 + ZZLSNaive_Aux(S, p , -k)
        if b < a:
            return a 
        else:
            return b
        #End if 
    else:
        return 0
    #End else 
#End def 
def NextElement(S, i, k):
    p = i + 1
    while(p < len(S) and (S[i] - S[p])*k>=0):
        p += 1
    #End while
    return p
#End def

#Memoizado
def ZZLSMemWrap(S):
    M = [[-math.inf for j in range(2)] for i in range(len(S))]
    p = ZZLSMem_Aux(S, 0, 1, M)
    n = ZZLSMem_Aux(S, 0, -1, M)
    if n < p:
        return p
    else: 
        return n 
    #End if
#End def 
def ZZLSMem_Aux(S, i, k, M):
    if i >= len(S): return 0
    if k == -1:
        kIndex = 0
    else:
        kIndex = 1
    if M[i][kIndex] == -math.inf:
        if i < len(S):
            p = NextElement(S, i, k)
            a = ZZLSMem_Aux(S, i + 1, k, M)
            b = 1 + ZZLSMem_Aux(S, p , -k, M)
            if b < a:
                M[i][kIndex] = a 
            else:
                M[i][kIndex] = b
            #End if 
        else:
            M[i][kIndex] = 0
        #End else 
    #End if 
    return M[i][kIndex]
#End def 

#Bootom-Up
def ZZLSBootom(S):
    M = [[0 for j in range(2)] for i in range(len(S) + 1)]
    for i in range (len(S), -1, -1):
        for k in range (-1,2, 2):
            if k == -1:
                kIndex = 0
            else:
                kIndex = 1
            #End if
            if i < len(S):
                p = NextElement(S, i, k)
                a = M[i + 1][kIndex]
                if kIndex == 0: 
                    auxIndex = 1
                else :
                    auxIndex = 0
                #End if
                b = 1 + M[p][auxIndex]
                if b < a:
                    M[i][kIndex] = a 
                else:
                    M[i][kIndex] = b
                #End if 
        #End for 
    #End for
    return max(M[0][0], M[0][1])
#End def

#BackTracking
def ZZLS(S):
    M = [[0 for j in range(2)] for i in range(len(S) + 1)]
    BT = [[(0,0) for j in range(2)] for i in range(len(S) + 1)]
    for i in range (len(S), -1, -1):
        for k in range (-1,2, 2):
            if k == -1:
                kIndex = 0
            else:
                kIndex = 1
            #End if
            if i < len(S):
                p = NextElement(S, i, k)
                a = M[i + 1][kIndex]
                if kIndex == 0: 
                    auxIndex = 1
                else :
                    auxIndex = 0
                #End if
                b = 1 + M[p][auxIndex]
                if b < a:
                    M[i][kIndex] = a
                    BT[i][kIndex] = (i + 1, k) 
                else:
                    M[i][kIndex] = b
                    BT[i][kIndex] = (p, -k)
                #End if 
        #End for 
    #End for
    if (M[0][0] > M[0][1]):
        k = 0
    else:
        k = 1
    R = [S[BT[0][k][0] - 1]]
    jIndex = BT[0][k][0]
    kIndex = BT[0][k][1]
    k += 1
    for i in range(1, len(BT) - 2):
        if jIndex < BT[i][k%2][0] and BT[i][k%2][1] != kIndex:
            R.append(S[BT[i][k%2][0] - 1])
            jIndex = BT[i][k%2][0]
            kIndex = BT[i][k%2][1]
            k += 1
        #End if
    #End for
    return max(M[0][0], M[0][1]),R
#End def

S = [10, 22, 9, 33, 49, 50, 31, 60]
print(f"Según el algoritmo naive, el tamaño máximo es {ZZLSNaiveWrap(S)}")
print(f"Según el algoritmo memoizado, el tamaño máximo es {ZZLSMemWrap(S)}")
print(f"Según el algoritmo Bottom-Up, el tamaño máximo es {ZZLSBootom(S)}")
num, R = ZZLS(S)
print(f"Según el algoritmo BU con BT, el tamaño máximo es {num}")
print(f"La sequencia es: {R}")
#Naive 
def LIS_Aux (S, i):
    if i == 0:
        return 0
    else:
        sinI = LIS_Aux(S, i -1)
        encontrado = False
        j = i - 1
        while S[ i - 1 ] <= S[ j - 1 ] and j > 0:
            j -= 1
        #End while
        conI = LIS_Aux(S, j) + 1
        if sinI > conI:
            return sinI
        else:
            return conI
        #End if
    #End if
#End def
def LIS (S):
    return LIS_Aux(S, len(S))
#End def

#Memoizacion
def LISMem_Aux (S, i, M):
    if M[i] == -1:    
        if i == 0:
            M[i] = 0
        else:
            sinI = LISMem_Aux(S, i -1, M)
            encontrado = False
            j = i - 1
            while(j >= 0):
                if S[j - 1] < S[i - 1]:
                    break
                j -= 1
            #End while
            conI = LISMem_Aux(S, j, M) + 1
            if sinI > conI:
                M[i] = sinI
            else:
                M[i] = conI
            #End if
        #End if
    #End if
    return M[i]
#End def
def LISMem (S):
    M = [-1 for i in range(len(S) + 1)]
    return LISMem_Aux(S, len(S) - 1, M)
#End def

#Bottom-Up
def LISBottom(S):
    M = [0 for i in range(len(S) + 1)]
    for i in range(1, len(S) + 1):
        sinI = M[i -1]
        encontrado = False
        j = i - 1
        while(j>= 0):
            if S[j - 1] < S[i - 1]:
                break
            j -= 1
        #End while
        conI = M[j] + 1
        if sinI > conI:
            M[i] = sinI
        else:
            M[i] = conI
        #End if
    #End for
    return M[i]
#End def

#Bottom-Up Back Tracking
def LISBottomBack(S):
    M = [0 for i in range(len(S) + 1)]
    BT = [-1 for i in range(len(S) + 1)]
    for i in range( 1, len( S ) + 1 ):
        j = i - 1
        while S[ i - 1 ] <= S[ j - 1 ] and j > 0:
            j = j - 1
        # end while
        a = M[ i - 1 ]
        b = M[ j ] + 1
        if a < b:
            M[ i ] = b
            BT[ i ] = j
        else:
            M[ i ] = a
            BT[ i ] = -1
        # end if
    # end for
    lis = []
    for i in range(0, len(BT)):
        if BT[i] >= 1:
            lis.append(S[BT[i] - 1])
        #End if
    #End for
    return [M[len(S)],lis]
#End def
print( LISBottomBack( [] ) )
print( LISBottomBack( [ 40 ] ) )
print( LISBottomBack( [ 40, 20 ] ) )
print( LISBottomBack( [ 20, 40 ] ) )
print( LISBottomBack( [ 5, 2, 8, 6, 3, 6, 9, 7 ] ) )
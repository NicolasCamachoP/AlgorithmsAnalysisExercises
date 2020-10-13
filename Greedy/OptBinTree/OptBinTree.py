import math 

#Naive aproach 
def OptTreeNaive_Aux(P, Q, i, j):
    if j == i - 1:
        return Q[i - 1]
    else:
        min_value = math.inf
        for r in range(i, j + 1):
            left = OptTreeNaive_Aux(P, Q, i, r - 1)
            right = OptTreeNaive_Aux(P, Q, r + 1, j)
            w = getW(P, Q, i, j)
            total = left + right + w
            if total < min_value:
                min_value = total
            #End if
        #End for 
        return min_value
    #End if
#End def

def getW(P, Q, i, j):
    pl = 0
    ql = 0
    for l in range (i, j + 1):
        pl += P[l - 1]
    #End def
    for l in range (i - 1, j + 1):
        ql += Q[l]
    #End def
    return pl + ql
#End def

def OptTreeNaive(P, Q):
    return OptTreeNaive_Aux(P, Q, 1, len(P))
#End def


P = [0.15, 0.1, 0.05, 0.1, 0.2]
Q = [0.05, 0.1, 0.05, 0.05, 0.05, 0.1]

print(OptTreeNaive(P, Q))


        


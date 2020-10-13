"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
import math
def ClimbStaNaive(n):
    return ClimbStaNaive_Aux(0, n)
#End def

def ClimbStaNaive_Aux(i, j):
    if i > j:
        return 0
    else:
        if i == j : 
            return 1
        return ClimbStaNaive_Aux(i + 1, j) + ClimbStaNaive_Aux(i + 2, j)
    #End if
#End def

#Memoizado
def ClimbStaMem(n):
    M = [math.inf for x in range(n + 2)]
    return ClimbStaNaive_Aux(0, n)
#End def
def ClimbStaMem_Aux(i, j):
    if M[i] == math.inf:
        if i > j:
            M[i] = 0
        else:
            if i == j : 
                M[i] = 1
            else:
                M[i] = ClimbStaNaive_Aux(i + 1, j) + ClimbStaNaive_Aux(i + 2, j)
            #End if
        #End if
    #End if
    return M[i]
#End def

#Bottom-Up
def ClimbStaBottom(n):
    M = [0 for x in range(n)]
    M[0] = 1
    M[1] = 2 
    for i in range(2, n):
        M[i] = M[i - 1] + M[i - 2]
    #End for
    return M[n - 1]
#End def



    
#End def

print(ClimbStaNaive(4))
print(ClimbStaMem(4))
print(ClimbStaBottom(4))

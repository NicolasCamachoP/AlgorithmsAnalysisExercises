"""
    You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
    the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and 
    it will automatically contact the police if two adjacent houses were broken into on the same night.

    Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount 
    of money you can rob tonight without alerting the police.
"""

import math

def HouseRobNaive(C):
    return HouseRobNaive_Aux(C, 0)
#End def

def HouseRobNaive_Aux(C, i):
    if i >= len(C):
        return 0
    else:
        rob = C[i] + HouseRobNaive_Aux(C, i + 2)
        skip = HouseRobNaive_Aux(C, i + 1)
        if rob > skip:
            return rob
        else:
            return skip
        #End if
    #End if
#End def

#Memoizado
def HouseRobMem(C):
    M = [math.inf for x in range(len(C) + 2)]
    return HouseRobMem_Aux(C, 0, M)
#End def
def HouseRobMem_Aux(C, i, M):
    if M[i] == math.inf:
        if i >= len(C):
            M[i] = 0
        else:
            rob = C[i] + HouseRobMem_Aux(C, i + 2, M)
            skip = HouseRobMem_Aux(C, i + 1, M)
            if rob > skip:
                M[i] = rob
            else:
                M[i] = skip
            #End if
        #End if
    #End if
    return M[i]
#End def

#Bottom-Up
def HouseRobBottom(C):
    M = [0 for x in range(len(C) + 2)]
    for i in range (len(C) - 1, -1, -1):
        rob = C[i] + M[i + 2]
        skip = M[i + 1]
        if rob > skip:
            M[i] = rob
        else:
            M[i] = skip
        #End if
    #End for
    return M[0]
#End def

#BackTracking
def HouseRobBT(C):
    M = [0 for x in range(len(C) + 2)]
    BT = [0 for x in range(len(C))]
    for i in range (len(C) - 1, -1, -1):
        rob = C[i] + M[i + 2]
        skip = M[i + 1]
        if rob > skip:
            M[i] = rob
            BT[i] = 1
        else:
            M[i] = skip
            BT[i] = 0
        #End if
    #End for
    R = []
    i = 0
    while(i < len(BT)):
        if BT[i] == 1:
            R.append(i)
            i += 2
        else:
            i += 1
        #ENd def
    #End while
    return [M[0],R]
#End def

C = [1, 2, 3, 1, 2, 5, 3, 1, 2, 3, 1]
print(HouseRobNaive(C))
print(HouseRobMem(C))
print(HouseRobBottom(C))
sol = HouseRobBT(C)
print(sol[0])
print(sol[1])



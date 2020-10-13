"""
In a country popular for train travel, you have planned some train travelling one year in advance.
The days of the year that you will travel is given as an array days.  Each day is an integer from 1 to 365.

Train tickets are sold in 3 different ways:

a 1-day pass is sold for costs[0] dollars;
a 7-day pass is sold for costs[1] dollars;
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.  For example, if we get a 7-day pass on day 2, 
then we can travel for 7 days: day 2, 3, 4, 5, 6, 7, and 8.

Return the minimum number of dollars you need to travel every day in the given list of days.
"""
import math


def MinTickets_Naive(D, C):
    S = [False for x in range (1, 1 + D[len(D) - 1])]
    j = 0
    for i in range(len(D)):
        S[D[i] - 1] = True
    #End for
    return MinTickets_NaiveAux(0, S, C)
#End def

def MinTickets_NaiveAux(i, S, C):
    if i >=len(S):
        return 0 
    else:
        if S[i]:
            OneDay = MinTickets_NaiveAux(i + 1, S, C) + C[0]
            SevenDays = MinTickets_NaiveAux(i + 7, S, C) + C[1]
            ThirtyDays = MinTickets_NaiveAux(i + 30, S, C) + C[2]
            return min (OneDay, SevenDays, ThirtyDays)
        else:
            return MinTickets_NaiveAux(i + 1, S, C)
    #End if
#End def

#Memoizado
def MinTickets_Mem(D, C):
    S = [False for x in range (1, 1 + D[len(D) - 1])]
    M = [math.inf for x in range (1, 1 + D[len(D) - 1])]
    j = 0
    for i in range(len(D)):
        S[D[i] - 1] = True
    #End for
    return MinTickets_MemAux(0, S, C, M)
#End def

def MinTickets_MemAux(i, S, C, M):
    if i >= len(S):
        return 0
    else:
        if M[i] == math.inf:
            if S[i]:
                OneDay = MinTickets_MemAux(i + 1, S, C, M) + C[0]
                SevenDays = MinTickets_MemAux(i + 7, S, C, M) + C[1]
                ThirtyDays = MinTickets_MemAux(i + 30, S, C, M) + C[2]
                M[i] = min (OneDay, SevenDays, ThirtyDays)
            else:
                M[i] = MinTickets_MemAux(i + 1, S, C, M)
            #End if
        #End if
        return M[i]
    #End if
#End def

#Bottom-Up
def MinTickets_Bottom(D, C):
    S = [False for x in range (1, 1 + D[len(D) - 1])]
    M = [0 for x in range (1, 1 + D[len(D) - 1])]
    j = 0
    for i in range(len(D)):
        S[D[i] - 1] = True
    #End for
    for i in range(len(S) - 1, -1, -1):
        if S[i]:
            if i + 1 < len(S):
                OneDay = M[i + 1] + C[0]
            else:
                OneDay = C[0]
            if i + 7 < len(S):
                SevenDays = M[i + 7] + C[1]
            else:
                SevenDays = C[1]
            if i + 30 < len(S):
                ThirtyDays = M[i + 30] + C[2]
            else:
                ThirtyDays = C[2]
            M[i] = min (OneDay, SevenDays, ThirtyDays)
        else:
            if i + 1 < len(S):
                M[i] = M[i + 1]    
            #End if
        #End if
    #End for
    return M[0]
#End def
D = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
C = [2, 7, 15]
print(MinTickets_Naive(D, C))
print(MinTickets_Mem(D, C))
print(MinTickets_Bottom(D, C))
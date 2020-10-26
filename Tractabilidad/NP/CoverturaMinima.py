import itertools
import math

def MinCovGraf(V, E):
    MinSize = math.inf
    Min = ()
    notFound = True
    i = 1
    while i < len(V) and notFound:
        for com in itertools.combinations(V, i):
            if isCov(E, com) and len(com) < MinSize:
                MinSize = len(com)
                Min = com
                notFound = False
                break
            #End if
        #End for
        i += 1
    #End for
    return Min
#End def

def isCov(E, Aux):
    finished = False
    AuxSet = set()
    j = 0
    i = 0
    while j < len(Aux) and not finished :
        while i < len(E) and not finished:
            if Aux[j] == E[i][0] or Aux[j] == E[i][1]:
                AuxSet.add(E[i])
            #End if
            if len(AuxSet) == len(E):
                finished = True
            #End if
            i += 1
        #End for
        i = 0
        j += 1
    #End for
    return finished    
#End for

V = [1, 2, 3, 4, 5, 6, 7]
E = [(1, 2),(2, 3),(3, 5), (3, 4), (4, 5), (5, 6), (4, 7)]
print(MinCovGraf(V, E))


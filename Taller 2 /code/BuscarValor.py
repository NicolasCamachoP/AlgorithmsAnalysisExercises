def SimpleIndexOf(S,v):
    j = -1
    for i in range(0,len(S)):
        if S[i] == v:
            j = i
            break
        #end if
    #end for
    return j
#end def


import random

def Partition( S, p, r, v ):
    x = S[r]
    i = p - 1
    for j in range(p, r):
        if S[j] <= x:
            i = i + 1
            S[i], S[j] = S[j], S[i]
        # end if
    # end for
    S[i + 1], S[r] = S[r], S[i + 1]
    return i + 1

def RandomizedPartition( S, p, r, v):
    i = random.randint( p, r )
    S[ r ], S[ i ] = S[ i ], S[ r ]
    return Partition( S, p, r, v)
## end def


def QuickSortSearchAux(S, p, r, v ):
    if p < r:
        q = RandomizedPartition( S, p, r, v)
        if(S[q] == v):
            return q
        elif S[q] > v:
           return QuickSortSearchAux( S, p, q - 1, v )
        else:
            return QuickSortSearchAux( S, q + 1, r, v )
    else:
        return S[r]
    ## end if
## end def

def QuickSortSearch( S,v ):
    return QuickSortSearchAux( S, 0, len( S ) - 1 , v)
## end def




S = [x for x in range(30,0,-1)]
v = 7
z = QuickSortSearch(S,v)
print(f'Se encontro el valor {v} en {z}: prueba -> {S[z]}')
print(S)
## eof - QuickSort.py


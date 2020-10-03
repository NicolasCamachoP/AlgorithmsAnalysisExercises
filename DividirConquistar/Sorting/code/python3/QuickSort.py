import random

## -------------------------------------------------------------------------
## QuickSortAux: sorts a subsequence of comparable (<) elements
## @inputs: S, a reference to a secuence of comparable elements.
##          p, start of the subsequence
##          r, end of the subsequence
## @outputs: S[p:r], an ordered permutation of the input.
## -------------------------------------------------------------------------
def Partition( S, p, r ):
    x = S[ r ]
    i = p
    for j in range( p, r ):
        if S[ j ] < x:
            S[ i ], S[ j ] = S[ j ], S[ i ]
            i += 1
        # end if
    # end for
    S[ i ], S[ r ] = S[ r ], S[ i ]
    return i
## end def

## -------------------------------------------------------------------------
## QuickSortAux: sorts a subsequence of comparable (<) elements
## @inputs: S, a reference to a secuence of comparable elements.
##          p, start of the subsequence
##          r, end of the subsequence
## @outputs: S[p:r], an ordered permutation of the input.
## -------------------------------------------------------------------------
def RandomizedPartition( S, p, r ):
    i = random.randint( p, r )
    S[ r ], S[ i ] = S[ i ], S[ r ]
    return Partition( S, p, r )
## end def

## -------------------------------------------------------------------------
## QuickSortAux: sorts a subsequence of comparable (<) elements
## @inputs: S, a reference to a secuence of comparable elements.
##          p, start of the subsequence
##          r, end of the subsequence
## @outputs: S[p:r], an ordered permutation of the input.
## -------------------------------------------------------------------------
def QuickSortAux( S, p, r ):
    if p < r:
        q = RandomizedPartition( S, p, r )
        QuickSortAux( S, p, q - 1 )
        QuickSortAux( S, q + 1, r )
    ## end if
## end def

## -------------------------------------------------------------------------
## QuickSort: sorts a sequence of comparable (<) elements
## @inputs: S, a reference to a secuence of comparable elements.
## @outputs: S, an ordered permutation of the input.
## -------------------------------------------------------------------------
def QuickSort( S ):
    QuickSortAux( S, 0, len( S ) - 1 )
## end def

## eof - QuickSort.py

## -------------------------------------------------------------------------
## BubbleSort: sorts a sequence of comparable (<) elements
## @inputs: S, a reference to a secuence of comparable elements.
## @outputs: S, an ordered permutation of the input.
## -------------------------------------------------------------------------
def BubbleSort( S ):
    for j in range( len( S ) ):
        for i in range( len( S ) - 1 ):
            if S[ i + 1 ] < S[ i ]:
                S[ i ], S[ i + 1 ] = S[ i + 1 ], S[ i ]
            ## end if
        ## end for
    ## end for
## end def

## eof - BubbleSort.py

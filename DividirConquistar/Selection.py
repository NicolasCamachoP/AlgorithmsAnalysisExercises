import random

class Selection:
    ## ---------------------------------------------------------------------
    def Naive( S, k ):
        C = [ S[ i ] for i in range( len( S ) ) ]
        C.sort( )
        return C[ k % len( S ) ]
    # end def

    ## ---------------------------------------------------------------------
    def Partition( S, p, r ):
        x = S[ r ]
        i = p - 1
        for j in range( p, r ):
            if S[ j ] <= x:
                i = i + 1
                S[ i ], S[ j ] = S[ j ], S[ i ]
            # end if
        # end for
        S[ i + 1 ], S[ r ] = S[ r ], S[ i + 1 ]
        return i + 1
    # end def

    ## ---------------------------------------------------------------------
    def RandomizedPartition( S, p, r ):
        i = random.randint( p, r )
        S[ r ], S[ i ] = S[ i ], S[ r ]
        return Selection.Partition( S, p, r )
    # end def

    ## ---------------------------------------------------------------------
    def DC_Aux( S, p, r, k ):
        if p >= r:
            return S[ p ]
        else:
            q = Selection.RandomizedPartition( S, p, r )
            if k == q:
                return S[ k ]
            elif k < q:
                return Selection.DC_Aux( S, p, q - 1, k )
            else:
                return Selection.DC_Aux( S, q + 1, r, k )
            # end if
        # end if
    # end def

    ## ---------------------------------------------------------------------
    def DC( S, k ):
        C = [ S[ i ] for i in range( len( S ) ) ]
        return Selection.DC_Aux( C, 0, len( C ) - 1, k % len( S ) )
    # end def
# end class

## -------------------------------------------------------------------------
if __name__ == "__main__":
    None
# end if

## eof - Selection.py

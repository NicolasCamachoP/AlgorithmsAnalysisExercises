import math

class Selection5:
    ## ---------------------------------------------------------------------
    def Sort( S, p, r ):
        for j in range( p + 1, r + 1 ):
            k = S[ j ]
            i = j - 1
            while p <= i and k < S[ i ]:
                S[ i + 1 ] = S[ i ]
                i = i - 1
            # end while
            S[ i + 1 ] = k;
        # end for
    # end def

    ## ---------------------------------------------------------------------
    def Partition( S, p, r, x ):
        i = p - 1
        q = -1
        for j in range( p, r + 1 ):
            if S[ j ] < x:
                i = i + 1
                S[ i ], S[ j ] = S[ j ], S[ i ]
            # end if
            if S[ j ] == x:
                q = j
            # end if
        # end for
        S[ i + 1 ], S[ q ] = S[ q ], S[ i + 1 ]
        return i + 1
    # end def

    ## ---------------------------------------------------------------------
    def DC_Aux( S, p, r, k ):
        if r <= p:
            return S[ p ]
        else:
            # 1. Divide and (insertion)-sort in 5-sized groups and get means
            n = math.ceil( ( r - p + 1 ) / 5 )
            X = [ 0 for i in range( n ) ]
            i = 0
            for a in range( p, r, 5 ):
                b = a + 4
                if b > r:
                    b = r
                # end if
                Selection5.Sort( S, a, b )
                X[ i ] = S[ int( ( a + b ) / 2 ) ]
                i = i + 1
            # end for

            # 2. Recursively, extract the mean of the means
            x = Selection5.DC_Aux( X, 0, n - 1, int( n / 2 ) )

            # 3. Perform partition
            q = Selection5.Partition( S, p, r, x )

            # 4. Analyze current configuration
            if q == k:
                return S[ k ]
            elif k < q:
                return Selection5.DC_Aux( S, p, q - 1, k )
            else:
                return Selection5.DC_Aux( S, q + 1, r, k )
            # end if
        # end if
    # end def

    ## ---------------------------------------------------------------------
    def DC( S, k ):
        C = [ S[ i ] for i in range( len( S ) ) ]
        return Selection5.DC_Aux( C, 0, len( C ) - 1, k % len( S ) )
    # end def
# end class

## ---------------------------------------------------------------------
if __name__ == "__main__":
    None
# end if

## eof - Selection.py

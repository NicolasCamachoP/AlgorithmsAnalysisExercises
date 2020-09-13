

## -------------------------------------------------------------------------
def Solve( X, Y ):
  M = [ [ 0 for j in range( len( Y ) + 1 ) ] for i in range( len( X ) + 1 ) ]
  B = [ [ [ 0, 0 ] for j in range( len( Y ) + 1 ) ] for i in range( len( X ) + 1 ) ]
  for i in range( 1, len( X ) + 1 ):
    for j in range( 1, len( Y ) + 1 ):
      if X[ i - 1 ] == Y[ j - 1 ]:
        M[ i ][ j ] = M[ i - 1 ][ j - 1 ] + 1
        B[ i ][ j ] = [ -1, -1 ]
      else:
        if M[ i ][ j - 1 ] < M[ i - 1 ][ j ]:
          M[ i ][ j ] = M[ i - 1 ][ j ]
          B[ i ][ j ] = [ -1, 0 ]
        else:
          M[ i ][ j ] = M[ i ][ j - 1 ]
          B[ i ][ j ] = [ 0, -1 ]
        # end if
      # end if
    # end for
  # end for

  # Backtracking
  Z = []
  [ i, j ] = [ len( X ), len( Y ) ]
  while i != 0 and j != 0:
    if B[ i ][ j ][ 0 ] == B[ i ][ j ][ 1 ]:
      Z = [ X[ i - 1 ] ] + Z
    # end if
    [ i, j ] = [ i + B[ i ][ j ][ 0 ], j + B[ i ][ j ][ 1 ] ]
  # end while
  return [ M[ len( X ) ][ len( Y ) ], Z ]
# end def

## eof - LCS.py

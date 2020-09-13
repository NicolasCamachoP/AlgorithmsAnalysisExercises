import math

## -------------------------------------------------------------------------
def Backtracking( R, i, j ):
  if i == j:
    return "A" + str( i )
  else:
    l = Backtracking( R, i, R[ i ][ j ] )
    r = Backtracking( R, R[ i ][ j ] + 1, j )
    s = ""
    if l.find( "x" ) != -1:
      s += "(" + l + ")"
    else:
      s += l
    # end if
    s += " x "
    if r.find( "x" ) != -1:
      s += "(" + r + ")"
    else:
      s += r
    # end if
    return s
  # end if
# end def

## -------------------------------------------------------------------------
def Solve( D ):
  M = [ [ 0 for j in range( len( D ) ) ] for i in range( len( D ) ) ]
  R = [ [ 0 for j in range( len( D ) ) ] for i in range( len( D ) ) ]
  for i in range( len( D ) - 1, 0, -1 ):
    for j in range( i + 1, len( D ) ):
      M[ i ][ j ] = math.inf
      for k in range( i, j ):
        v = M[ i ][ k ] + M[ k + 1 ][ j ] + D[ i - 1 ] * D[ k ] * D[ j ]
        if v < M[ i ][ j ]:
          M[ i ][ j ] = v
          R[ i ][ j ] = k
        # end if
      # end for
    # end for
  # end for
  return [ M[ 1 ][ len( D ) - 1 ], Backtracking( R, 1, len( D ) - 1 ) ]
## end def

## eof - MatChain.py

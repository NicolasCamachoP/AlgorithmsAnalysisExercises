
import math

def PrintMatrix( M ):
  for j in range( len( M ) ):
    for i in range( len( M ) ):
      if M[ i ][ j ] == math.inf:
        print( ".", end = "" )
      else:
        print( "x", end = "" )
    # end for
    print( "" )
  # end for
  print( "---------------------" )
# end def

def MatrixMult_Aux( D, i, j, M ):
  if M[ i ][ j ] == math.inf:
    if i == j:
      M[ i ][ j ] = 0
      PrintMatrix( M )
    else:
      q = math.inf
      for k in range( i, j ):
        left = MatrixMult_Aux( D, i, k, M )
        right = MatrixMult_Aux( D, k + 1, j, M )
        m = left + right + ( D[ i - 1 ] * D[ k ] * D[ j ] )
        if m < q:
          q = m
        # end if
      # end for
      M[ i ][ j ] = q
      PrintMatrix( M )
    # end if
  # end if
  return M[ i ][ j ]
# end def

def MatrixMult( D ):
  M = [ [ math.inf for i in range( len( D ) ) ] for j in range( len( D ) )  ]
  return MatrixMult_Aux( D, 1, len( D ) - 1, M )
# end def

D = [ 10, 100, 5, 50, 3, 2, 10, 125, 35, 246 ]
print( MatrixMult( D ) )

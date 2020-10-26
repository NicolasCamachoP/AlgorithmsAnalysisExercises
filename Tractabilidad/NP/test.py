## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import math, random, sys
import HamiltonLoop

## -------------------------------------------------------------------------

## Build graph
if len( sys.argv ) == 1:
  points = [
    [ 1, 0 ],
    [ 1, 2 ],
    [ 0, 3 ],
    [ 3, 0 ],
    [ 4, 1 ],
    [ 3, 2 ],
    [ 5, 2 ],
    [ 2, 4 ]
    ]
else:
  points = []
  for i in range( int( sys.argv[ 1 ] ) ):
    points.append( [ random.uniform( -100, 100 ), random.uniform( -100, 100 ) ] )
  # end for
# end if
n = len( points )
edges = [ [ 0 for j in range( n ) ] for i in range( n ) ]
for i in range( n ):
  for j in range( i + 1, n ):
    c =     ( points[ i ][ 0 ] - points[ j ][ 0 ] ) ** 2
    c = c + ( points[ i ][ 1 ] - points[ j ][ 1 ] ) ** 2
    c = math.sqrt( c )
    edges[ i ][ j ] = c
    edges[ j ][ i ] = c
  # end for
# end for

bf = HamiltonLoop.BruteForce( points, edges )
print( len( bf[ 1 ] ), bf[ 0 ] )
print( "------------------------------" )
for i in range( len( points ) ):
  ap = HamiltonLoop.Approximation2( points, edges, i )
  print( len( ap[ 1 ] ), ( ap[ 0 ] / bf[ 0 ] ) )
# end for

## eof - test.py

## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import itertools, math, random
import Dijkstra

## -------------------------------------------------------------------------
def BruteForce( V, A ):
  best_loop_cost = math.inf
  best_loop = []
  for p in itertools.permutations( list( range( len( V ) ) ) ):
    c = 0
    i = 0
    stop = False
    loop = []
    while i < len( p ) and not stop:
      j = ( i + 1 ) % len( p )
      if A[ p[ i ] ][ p[ j ] ] != math.inf:
        c = c + A[ p[ i ] ][ p[ j ] ]
        loop.append( V[ p[ i ] ] )
      else:
        stop = True
      # end if
      i = i + 1
    # end while
    if not stop:
      if c < best_loop_cost:
        best_loop_cost = c
        best_loop = loop
      # end if
    # end if
  # end for
  return [ best_loop_cost, best_loop ]
# end def

## -------------------------------------------------------------------------
def Approximation2( V, A, r = None ):
  if r == None:
    r = random.randint( 0, len( V ) - 1 )
  # end if
  mst = Dijkstra.Compute( V, A, r )
  loop_idx = Dijkstra.PreOrder( mst, r )
  loop = []
  c = 0
  for i in range( len( loop_idx ) ):
    c = c + A[ loop_idx[ i ] ][ loop_idx[ ( i + 1 ) % len( loop_idx ) ] ]
    loop.append( V[ loop_idx[ i ] ] )
  # end for
  return [ c, loop ]
# end def

## eof - HamiltonLoop.py

## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import heapq, math

## -------------------------------------------------------------------------
'''
Structure that holds dijkstra nodes
'''
class Node( object ):
  # --
  def __init__( self, v, p, c ):
    self.m_Vertex = v
    self.m_Parent = p
    self.m_Cost = c
  # end def

  # --
  def __repr__( self ):
    return 'Node value: {self.m_Vertex}'
  # end def

  # --
  def __lt__( self, right ):
    return self.m_Cost < right.m_Cost
  # end def
# end class

## -------------------------------------------------------------------------
def Compute( V, A, s ):

  # Configure auxiliary data structures
  marks = [ False for i in range( len( V ) ) ]
  tree = [ -1 for i in range( len( V ) ) ]
  queue = [ Node( s, s, 0 ) ]

  # Main loop
  while len( queue ) > 0:

    # Get next node
    n = heapq.heappop( queue )

    # Check if it has been already visited
    if not marks[ n.m_Vertex ]:

      # Mark current node
      marks[ n.m_Vertex ] = True

      # Update tree
      tree[ n.m_Vertex ] = n.m_Parent

      # Add neighbors
      for i in range( len( V ) ):
        if A[ n.m_Vertex ][ i ] != math.inf and not marks[ i ]:
          heapq.heappush(
            queue,
            Node( i, n.m_Vertex, A[ n.m_Vertex ][ i ] + n.m_Cost )
            )
        # end if
      # end for

    # end if
  # end while

  # Return spanning tree
  return tree
# end def

## -------------------------------------------------------------------------
def Backtrack( V, A, T, e ):
  if T[ e ] >= 0:
    p = []
    i = e
    c = 0
    while T[ i ] != i:
      p.insert( 0, V[ i ] )
      c = c + A[ T[ i ] ][ i ]
      i = T[ i ]
    # end while
    p.insert( 0, V[ i ] )
    return [ p, c ]
  else:
    return [ [], math.inf ]
  # end if
# end def

## -------------------------------------------------------------------------
def PreOrder( T, r ):
  p = [ r ]
  for i in range( len( T ) ):
    if T[ i ] == r and i != r:
      p.extend( PreOrder( T, i ) )
    # end if
  # end for
  return p
# end def

## eof - Dijkstra.py

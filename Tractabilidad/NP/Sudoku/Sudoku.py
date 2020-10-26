import copy, itertools, math, re, sys

## -------------------------------------------------------------------------
class Sudoku:

  # ------------------------------------------------------------------------
  def print_board( board ):
    for i in range( len( board ) ):
      if i % 3 == 0:
        print( "+-------+-------+-------+" )
      # end if
      for j in range( len( board ) ):
        if j % 3 == 0:
          print( "|", end = " " )
        # end if
        print( board[ i ][ j ], end = " " )
      # end for
      print( "|" )
    # end for
    print( "+-------+-------+-------+" )
  # end def

  # ------------------------------------------------------------------------
  def is_valid( board ):
    # Check rows
    cr = True
    r = 0
    j = 0
    while r < 9 and cr:
      rows = [ 0 for i in range( 10 ) ]
      while j < 9 and cr:
        v = board[ r ][ j ]
        rows[ v ] += 1
        if rows[ v ] > 1 and v != 0 :
          cr = False
        # end if
        j += 1
      # end while
      r += 1
      j = 0
    # end while

    #If rows check fails, interrupt the process
    if(not cr):
      return False
    
    # Check columns
    cc = True
    c = 0
    i = 0
    while c < 9 and cc:
      cols = [ 0 for i in range( 10 ) ]
      while i < 9 and cc:
        v = board[ i ][ c ]
        cols[ v ] += 1
        if cols[ v ] > 1 and v != 0 :
          cc = False
        # end if
        i += 1
      # end while
      c += 1
      i = 0
    # end while

    #If col check fails, interrupt the process
    if(not cc):
      return False

    # Check blocks
    cb = True
    i = 0
    j = 0
    while i < 3 and cb:
      while j < 3 and cb:
        blocks = [ 0 for m in range( 10 ) ]
        for k in range( 3 * i, 3 * ( i + 1 ) ):
          for l in range( 3 * j, 3 * ( j + 1 ) ):
            v = board[ k ][ l ]
            blocks[ v ] += 1
            if blocks[ v ] > 1 and v != 0 :
              cb = False
            # end if
          # end for
        # end for
        j += 1
      # end while
      i += 1
      j = 0
    # end while
    return cb
  # end def

  # ------------------------------------------------------------------------
  def is_full( board ):
    s = True
    i = 0
    j = 0
    while i < 9 and s:
      while j < 9 and s:
        if board[ i ][ j ] == 0:
          s = False
        # end if
        j += 1
      # end while
      i += 1
      j = 0
    # end while
    return s
  #  end def

  # ------------------------------------------------------------------------
  def read_file( fname ):
    board = [ [ 0 for i in range( 9 ) ] for j in range( 9 ) ]
    f = open( fname, 'r' )
    row = 0
    for line in f:
      if line[ 0 ] == '|':
        tokens = re.split( ' ', line.replace( '|', '' ).replace( '\n', '' ) )
        col = 0
        for t in tokens:
          if t != '':
            board[ row ][ col ] = int( t )
            col = col + 1
          # end if
        # end for
        row = row + 1
      # end if
    # end for
    f.close( )
    return board
  # end def
    
  # ------------------------------------------------------------------------
  def solve_BF( board ):
    # Count missing values
    counts = [ 9 for i in range( 10 ) ]
    positions = []
    for i in range( 9 ):
      for j in range( 9 ):
        counts[ board[ i ][ j ] ] -= 1
        if board[ i ][ j ] == 0:
          positions.append( [ i, j ] )
        # end if
      # end for
    # end for

    # Create options
    options = []
    for i in range( 1, 10 ):
      for j in range( counts[ i ] ):
        options.append( i )
      # end for
    # end for
    print(
      "Number of empty cells: {:d} ({:.3f}%)".format(
        len( options ), float( len( options ) ) / 0.81
        )
      )
    should_continue = input( "Continue? [Y/N] " )
    if should_continue == 'n' or should_continue == 'N':
      return None
    # end if

    # Iterate
    count = 1
    total = math.factorial( len( options ) )
    for s in itertools.permutations( options ):
      if count % 10000 == 0:
        print(
          "Trying: {:.2f}%".format(
            ( float( 100 ) * float( count ) / float( total ) )
            )
          )
      # end if
      count += 1
      test = copy.deepcopy( board )
      for i in range( len( s ) ):
        test[ positions[ i ][ 0 ] ][ positions[ i ][ 1 ] ] = s[ i ]
      # end for
      if Sudoku.is_valid( test ):
        print(
          "Tried: {:d} of {:d} total cases.".format( count, total )
          )
        return test
      # end if
    # end for
    return None
  # end def

  # ------------------------------------------------------------------------
  def solve_H0_aux( board, positions, i ):
    if len( positions ) == i:
      return Sudoku.is_valid( board )
    else:
      p = positions[ i ]
      v = 1
      stop = False
      while v < 10 and not stop:
        board[ p[ 0 ] ][ p[ 1 ] ] = v
        if Sudoku.is_valid( board ):
          if Sudoku.solve_H0_aux( board, positions, i + 1 ):
            stop = True
          else:
            v = v + 1
        else:
          v = v + 1
        # end if
      # end while
      if stop:
        return True
      else:
        board[ p[ 0 ] ][ p[ 1 ] ] = 0
        return False
      # end if
    # end if
  # end def

  # ------------------------------------------------------------------------
  def solve_H0( board ):
    # Find missing positions
    positions = []
    for i in range( 9 ):
      for j in range( 9 ):
        if board[ i ][ j ] == 0:
          positions.append( [ i, j ] )
        # end if
      # end for
    # end for
    return Sudoku.solve_H0_aux( board, positions, 0 )
  # end def
# end class

## -------------------------------------------------------------------------
## -- Test
board = Sudoku.read_file( sys.argv[ 1 ] )
print( "====================================" )
Sudoku.print_board( board )
if sys.argv[ 2 ] == "bf":
  solution = Sudoku.solve_BF( board )
  if solution != None:
    print( "====================================" )
    Sudoku.print_board( solution )
  else:
    print( "********************************************" )
    print( "************* UNSOLVABLE BOARD *************" )
    print( "********************************************" )
  # end if
else:
  if Sudoku.solve_H0( board ):
    print( "====================================" )
    Sudoku.print_board( board )
  else:
    print( "********************************************" )
    print( "************* UNSOLVABLE BOARD *************" )
    print( "********************************************" )
  # end if
# end if

## eof - Sudoku.py


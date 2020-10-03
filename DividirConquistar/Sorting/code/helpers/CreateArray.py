#!/usr/bin/python3

import random, struct, sys

## -------------------------------------------------------------------------
## Main code
## -------------------------------------------------------------------------

## Check arguments
if len( sys.argv ) < 3:
    print( "Usage: ", sys.argv[ 0 ], "file n [shuffle]" )
    exit( 1 )
## end if

n = int( sys.argv[ 2 ] )
S = [ i for i in range( n ) ]
if len( sys.argv ) > 3:
    random.shuffle( S )
# end if

out = open( sys.argv[ 1 ], "w" )
out.write( str( len( S ) ) + "\n" )
for s in S:
    out.write( str( s ) + "\n" )
# end for
out.close( )

## eof - CreateRandomArray.py

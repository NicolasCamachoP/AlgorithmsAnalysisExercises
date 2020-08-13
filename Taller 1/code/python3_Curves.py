#!/usr/bin/python3

import random, sys, time
import python3

## -------------------------------------------------------------------------
def IsSorted( S ):
    r = True
    for i in range( len( S ) - 1 ):
        if S[ i + 1 ] < S[ i ] and r:
            r = False
        ## end if
    ## end for
    return r
## end def

## -------------------------------------------------------------------------
def MeasureTime( alg, S ):
    sT = time.process_time( )
    alg( S )
    eT = time.process_time( )
    return float( eT - sT )
## end def
    
## -------------------------------------------------------------------------
## Main code
## -------------------------------------------------------------------------

## Check arguments
if len( sys.argv ) < 4:
    print( "Usage: ", sys.argv[ 0 ], "min_s max_s s_step [shuf]" )
    exit( 1 )
## end if

min_s = int( sys.argv[ 1 ] )
max_s = int( sys.argv[ 2 ] )
s_step = int( sys.argv[ 3 ] )
shuf = len( sys.argv ) > 4

for n in range( min_s, max_s + s_step, s_step ):
    print( n, file=sys.stderr )
    Sb = [ i for i in range( n ) ]
    if shuf:
        random.shuffle( Sb )
    # end if
    Si = Sb.copy( )
    Sq = Sb.copy( )

    ib = int( IsSorted( Sb ) )
    ii = int( IsSorted( Si ) )
    iq = int( IsSorted( Sq ) )

    tb = MeasureTime( python3.BubbleSort, Sb )
    ti = MeasureTime( python3.InsertionSort, Si )
    tq = MeasureTime( python3.QuickSort, Sq )

    print( str( n ) + " " + str( tb ) + " " + str( ti ) + " " + str( tq ) + " " + str( ib ) + " " + str( ii ) + " " + str( iq ) + " " + str( int( IsSorted( Sb ) ) ) + " " + str( int( IsSorted( Si ) ) ) + " " + str( int( IsSorted( Sq ) ) ) )

# end for

## eof - python3_Curves.py

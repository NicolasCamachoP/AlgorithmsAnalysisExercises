#!/usr/bin/python3

import sys, time
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
if len( sys.argv ) != 2:
    print( "Usage: ", sys.argv[ 0 ], "file" )
    exit( 1 )
## end if

Sb = []
Si = []
Sq = []
with open( sys.argv[ 1 ] ) as f:
    n = int( next( f ) )
    for line in f:
        Sb.append( [ int( x ) for x in line.split( ) ][ 0 ] )
        Si.append( Sb[ len( Sb ) - 1 ] )
        Sq.append( Sb[ len( Sb ) - 1 ] )
    # end for
# end with

ib = IsSorted( Sb )
ii = IsSorted( Si )
iq = IsSorted( Sq )

tb = MeasureTime( python3.BubbleSort, Sb )
ti = MeasureTime( python3.InsertionSort, Si )
tq = MeasureTime( python3.QuickSort, Sq )

print( "Bubble    : " + str( tb ) + "\t(" + str( IsSorted( Sb ) ) + ")\t(" + str( ib ) + ")" )
print( "Insertion : " + str( ti ) + "\t(" + str( IsSorted( Si ) ) + ")\t(" + str( ii ) + ")" )
print( "Quicksort : " + str( tq ) + "\t(" + str( IsSorted( Sq ) ) + ")\t(" + str( iq ) + ")" )

## Write results
f = open( "python3_bubble.txt", "w" )
for v in Sb:
    f.write( str( v ) + "\n" )
# end for
f.close( )

f = open( "python3_insertion.txt", "w" )
for v in Si:
    f.write( str( v ) + "\n" )
# end for
f.close( )

f = open( "python3_quick.txt", "w" )
for v in Sq:
    f.write( str( v ) + "\n" )
# end for
f.close( )

## eof - python3_Experiments.py

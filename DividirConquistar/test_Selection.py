import random, sys, time
from Selection import *
from Selection5 import *

n = 11
k = 5
if len( sys.argv ) > 1:
    n = int( sys.argv[ 1 ] )
# end if
if len( sys.argv ) > 2:
    k = int( sys.argv[ 2 ] )
# end if
start_fill = time.time( )
A = [ random.randint( 0, 10000 ) for i in range( n ) ]
t_fill = time.time( ) - start_fill

start_naive = time.time( )
naive = Selection.Naive( A, k )
t_naive = time.time( ) - start_naive

start_dc = time.time( )
dc = Selection.DC( A, k )
t_dc = time.time( ) - start_dc

start_5 = time.time( )
k_5 = Selection5.DC( A, k )
t_5 = time.time( ) - start_5

print( "Fill time          : ", t_fill, "s" )
print( "Naive              : ", naive, "(", t_naive, "s )" )
print( "Divide-and-conquer : ", dc, "(", t_dc, "s )" )
print( "Worst-case linear  : ", k_5, "(", t_5, "s )" )

# eof - test_selection.py


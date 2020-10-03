
#include "c/SortFunctions.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main( int argc, char* argv[] )
{
  FILE* file;
  int n, i;

  /* Read file */
  file = fopen( argv[ 1 ], "r" );
  fscanf( file, "%d", &n );
  int* Sb = ( int* )( malloc( n * sizeof( int ) ) );
  int* Si = ( int* )( malloc( n * sizeof( int ) ) );
  int* Sq = ( int* )( malloc( n * sizeof( int ) ) );
  for( i = 0; i < n; i++ )
  {
    fscanf( file, "%d", Sb + i );
    Si[ i ] = Sq[ i ] = Sb[ i ];
  } /* end for */
  fclose( file );

  int ib = IsSorted( Sb, n );
  int ii = IsSorted( Si, n );
  int iq = IsSorted( Sq, n );

  /* Sort! */
  time_t start, end;

  time( &start );
  BubbleSort( Sb, n );
  time( &end );
  double tb = ( double )( end - start );

  time( &start );
  InsertionSort( Si, n );
  time( &end );
  double ti = ( double )( end - start );

  time( &start );
  QuickSort( Sq, n );
  time( &end );
  double tq = ( double )( end - start );

  /* Show */
  printf( "Bubble    : %.10f\t(%d)\t(%d)\n", tb, IsSorted( Sb, n ), ib );
  printf( "Insertion : %.10f\t(%d)\t(%d)\n", ti, IsSorted( Si, n ), ii );
  printf( "QuickSort : %.10f\t(%d)\t(%d)\n", tq, IsSorted( Sq, n ), iq );

  /* Save results */
  file = fopen( "c_bubble.txt", "w" );
  for( i = 0; i < n; i++ )
    fprintf( file, "%d\n", Sb[ i ] );
  fclose( file );

  file = fopen( "c_insertion.txt", "w" );
  for( i = 0; i < n; i++ )
    fprintf( file, "%d\n", Si[ i ] );
  fclose( file );

  file = fopen( "c_quick.txt", "w" );
  for( i = 0; i < n; i++ )
    fprintf( file, "%d\n", Sq[ i ] );
  fclose( file );

  free( Sb );
  free( Si );
  free( Sq );
  return( 0 );
}

/* eof - c_Experiments.c */

#include "SortFunctions.h"

void InsertionSort( int* S, int N )
{
  int i, j, k;
  for( j = 2; j <= N; j++ )
  {
    k = S[ j - 1 ];
    i = j - 1;
    while( 0 < i && k < S[ i - 1 ] )
    {
      S[ i ] = S[ i - 1 ];
      i = i - 1;
    } /* end while */
    S[ i ] = k;
  } /* end for */
}

/* eof - InsertionSort.c */

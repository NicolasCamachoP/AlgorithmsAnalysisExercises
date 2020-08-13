#include "SortFunctions.h"
#include <stdio.h>

void BubbleSort( int* S, int N )
{
  int i, j, aux;
  for( j = 0; j < N; j++ )
  {
    for( i = 0; i < N - 1; i++ )
    {
      if( S[ i + 1 ] < S[ i ] )
      {
        aux = S[ i ];
        S[ i ] = S[ i + 1 ];
        S[ i + 1 ] = aux;
      } /* end if */
    } /* end for */
  } /* end for */
}

/* eof - BubbleSort.c */

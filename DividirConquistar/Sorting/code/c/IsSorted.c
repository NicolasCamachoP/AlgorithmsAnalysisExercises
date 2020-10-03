#include "SortFunctions.h"
#include <stdio.h>

int IsSorted( int* S, int N )
{
  int i, is_sorted = 1;
  for( i = 1; i < N; i++ )
  {
    if( S[ i ] < S[ i - 1 ] && is_sorted == 1 )
      is_sorted = 0;
  } /* end for */
  return( is_sorted );
}

/* eof - IsSorted.c */

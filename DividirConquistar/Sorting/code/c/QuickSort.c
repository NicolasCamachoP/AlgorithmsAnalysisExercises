#include <stdlib.h>
#include "SortFunctions.h"

/* -------------------------------------------------------------------------
 * RandInterval: Get an uniformly distributed random number
 * @inputs: min, start of the range
 *          max, end of the range
 * @outputs: min <= q <= max
 * -------------------------------------------------------------------------
 */
int RandInterval( int min, int max )
{
  int r;
  const int range = 1 + max - min;
  const int buckets = RAND_MAX / range;
  const int limit = buckets * range;
  do
  {
    r = rand( );
  } while( r >= limit );
  return( min + ( r / buckets ) );
}

/* -------------------------------------------------------------------------
 * Partition: permutes a sequence around a pivot located in position r.
 * @inputs: S, a reference to a secuence of comparable elements.
 *          p, start of the subsequence
 *          r, end of the subsequence (and pivot)
 * @outputs: S[p:q) are the elements less than S[q], and S(q,r] are the
 *           elements greater than S[q]
 * -------------------------------------------------------------------------
 */
int Partition( int* S, int p, int r )
{
  int x, i, j, aux;

  x = S[ r ];
  i = p;
  for( j = p; j < r; j++ )
  {
    if( S[ j ] < x )
    {
      aux = S[ i ];
      S[ i ] = S[ j ];
      S[ j ] = aux;
      i = i + 1;
    } /* end if */
  } /* end for */

  aux = S[ i ];
  S[ i ] = S[ r ];
  S[ r ] = aux;

  return( i );
}

/* -------------------------------------------------------------------------
 * RandomPartition: randomly selects a pivot and partitions S around it.
 * @inputs: S, a reference to a secuence of comparable elements.
 *          p, start of the subsequence
 *          r, end of the subsequence
 * @outputs: S[p:q) are the elements less than S[q], and S(q,r] are the
 *           elements greater than S[q]
 * -------------------------------------------------------------------------
 */
int RandomPartition( int* S, int p, int r )
{
  int i, aux;

  i = RandInterval( p, r );
  aux = S[ r ];
  S[ r ] = S[ i ];
  S[ i ] = aux;
  return( Partition( S, p, r ) );
}

/* -------------------------------------------------------------------------
 * QuickSortAux: sorts a subsequence of comparable (<) elements
 * @inputs: S, a reference to a secuence of comparable elements.
 *          p, start of the subsequence
 *          r, end of the subsequence
 * @outputs: S[p:r], an ordered permutation of the input.
 * -------------------------------------------------------------------------
 */
void QuickSortAux( int* S, int p, int r )
{
  int q;
  if( p < r )
  {
    q = RandomPartition( S, p, r );
    QuickSortAux( S, p, q - 1 );
    QuickSortAux( S, q + 1, r );
  } /* end if */
}

/* ---------------------------------------------------------------------- */
void QuickSort( int* S, int N )
{
  QuickSortAux( S, 0, N - 1 );
}

/* eof - QuickSort.c */

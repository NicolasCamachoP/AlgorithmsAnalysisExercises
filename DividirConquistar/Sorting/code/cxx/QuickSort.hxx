#ifndef __QuickSort__hxx__
#define __QuickSort__hxx__

#include <algorithm>
#include <iterator>
#include <random>

/* -------------------------------------------------------------------------
 * Partition: permutes a sequence around a pivot located in position r.
 * @inputs: S, a reference to a secuence of comparable elements.
 *          p, start of the subsequence
 *          r, end of the subsequence (and pivot)
 * @outputs: S[p:q) are the elements less than S[q], and S(q,r] are the
 *           elements greater than S[q]
 * -------------------------------------------------------------------------
 */
template< class _TIt >
_TIt Partition( _TIt b, _TIt e )
{
  auto x = *( e - 1 );
  _TIt i = b;
  for( _TIt j = b; j != e; j++ )
  {
    if( *j < x )
    {
      std::iter_swap( i, j );
      i++;
    } // end if
  } // end for

  // Pivot
  std::iter_swap( i, e - 1 );

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
template< class _TIt >
_TIt RandomPartition( _TIt b, _TIt e, long n )
{
  static std::random_device r;
  static std::mt19937 g( r( ) );
  std::uniform_int_distribution< long > d( 0, n - 1 );
  _TIt i = b + d( g );
  std::iter_swap( i, e - 1 );
  return( Partition( b, e ) );
}

// -------------------------------------------------------------------------
template< class _TIt >
void QuickSort( _TIt b, _TIt e )
{
  long n = std::distance( b, e );
  if( n > 1 )
  {
    _TIt q = RandomPartition( b, e, n );
    QuickSort( b, q );
    QuickSort( q + 1, e );
  } // end if
}

#endif // __QuickSort__hxx__

// eof - QuickSort.hxx

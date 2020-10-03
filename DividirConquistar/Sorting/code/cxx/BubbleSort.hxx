#ifndef __BubbleSort__hxx__
#define __BubbleSort__hxx__

#include <algorithm>
#include <iterator>

template< class _TIt >
void BubbleSort( _TIt b, _TIt e )
{
  unsigned int n = std::distance( b, e );
  for( unsigned long j = 0; j < n; ++j )
  {
    for( _TIt i = b; i + 1 != e; i++ )
      if( *( i + 1 ) < *i )
        std::iter_swap( i, i + 1 );
  } // end for
}

#endif // __BubbleSort__hxx__

// eof - BubbleSort.hxx

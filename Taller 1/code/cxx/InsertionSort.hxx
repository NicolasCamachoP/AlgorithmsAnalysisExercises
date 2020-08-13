#ifndef __InsertionSort__hxx__
#define __InsertionSort__hxx__

#include <iostream>

template< class _TIt >
void InsertionSort( _TIt b, _TIt e )
{
  for( _TIt j = b + 1; j != e; j++ )
  {
    auto k = *j;
    _TIt i = j - 1;
    bool stop = false;
    while( !stop && k < *i )
    {
      stop = ( i == b );
      *( i + 1 ) = *i;
      i = i - 1;
    } // end while
    *( i + 1 ) = k;
  } // end for
}

#endif // __InsertionSort__hxx__

// eof - InsertionSort.hxx

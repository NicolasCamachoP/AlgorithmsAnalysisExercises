#ifndef __IsSorted__hxx__
#define __IsSorted__hxx__

template< class _TIt >
bool IsSorted( _TIt b, _TIt e )
{
  bool is_sorted = true;
  for( _TIt i = b + 1; i != e; ++i )
    is_sorted &= !( *i < *( i - 1 ) );
  return( is_sorted );
}

#endif // __IsSorted__hxx__

// eof - IsSorted.hxx

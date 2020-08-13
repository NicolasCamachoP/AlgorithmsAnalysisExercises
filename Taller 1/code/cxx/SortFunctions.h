#ifndef __SortFunctions__h__
#define __SortFunctions__h__

/** ------------------------------------------------------------------------
 * BubbleSort: sorts a sequence of comparable (<) elements
 * @inputs: b, e two iterators on the sequence
 * @outputs: the range [b,e] has been ordered
 * -------------------------------------------------------------------------
 */
template< class _TIt >
void BubbleSort( _TIt b, _TIt e );

/** ------------------------------------------------------------------------
 * InsertionSort: sorts a sequence of comparable (<) elements
 * @inputs: b, e two iterators on the sequence
 * @outputs: the range [b,e] has been ordered
 * -------------------------------------------------------------------------
 */
template< class _TIt >
void InsertionSort( _TIt b, _TIt e );

/** ------------------------------------------------------------------------
 * QuickSort: sorts a sequence of comparable (<) elements
 * @inputs: b, e two iterators on the sequence
 * @outputs: the range [b,e] has been ordered
 * -------------------------------------------------------------------------
 */
template< class _TIt >
void QuickSort( _TIt b, _TIt e );

/** ------------------------------------------------------------------------
 * IsSorted: Informs if a sequence is ordered
 * @inputs: b, e two iterators on the sequence
 * @outputs: true/false if sequence is ordered
 * -------------------------------------------------------------------------
 */
template< class _TIt >
bool IsSorted( _TIt b, _TIt e );

// -------------------------------------------------------------------------
#include "BubbleSort.hxx"
#include "InsertionSort.hxx"
#include "QuickSort.hxx"
#include "IsSorted.hxx"

#endif // __SortFunctions__h__

// eof - SortFunctions.h

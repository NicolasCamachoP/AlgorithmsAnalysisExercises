#ifndef __SortFunctions__h__
#define __SortFunctions__h__

/** ------------------------------------------------------------------------
 * BubbleSort: sorts a sequence of comparable (<) elements
 * @inputs: S, a reference to a secuence of comparable elements.
 * @outputs: S, an ordered permutation of the input.
 * -------------------------------------------------------------------------
 */
void BubbleSort( int* S, int N );

/** ------------------------------------------------------------------------
 * InsertionSort: sorts a sequence of comparable (<) elements
 * @inputs: S, a reference to a secuence of comparable elements.
 * @outputs: S, an ordered permutation of the input.
 * -------------------------------------------------------------------------
 */
void InsertionSort( int* S, int N );

/** ------------------------------------------------------------------------
 * QuickSort: sorts a sequence of comparable (<) elements
 * @inputs: S, a reference to a secuence of comparable elements.
 * @outputs: S, an ordered permutation of the input.
 * -------------------------------------------------------------------------
 */
void QuickSort( int* S, int N );

/** ------------------------------------------------------------------------
 * IsSorted: Informs if a sequence is ordered
 * @inputs: b, e two iterators on the sequence
 * @outputs: true/false if sequence is ordered
 * -------------------------------------------------------------------------
 */
int IsSorted( int* S, int N );

#endif /* __SortFunctions__h__ */

/* eof - SortFunctions.h */

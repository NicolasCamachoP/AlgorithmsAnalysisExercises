
#include "cxx/SortFunctions.h"

#include <chrono>
#include <fstream>
#include <iostream>
#include <vector>

int main( int argc, char* argv[] )
{
  // Read file
  std::ifstream file( argv[ 1 ] );
  unsigned long n;
  file >>n;
  std::vector< int > Sb( n ), Si( n ), Sq( n );
  for( unsigned long i = 0; i < n; i++ )
  {
    int v;
    file >> v;
    Sb[ i ] = Si[ i ] = Sq[ i ] = v;
  } // end for
  file.close( );

  bool ib = IsSorted( Sb.begin( ), Sb.end( ) );
  bool ii = IsSorted( Si.begin( ), Si.end( ) );
  bool iq = IsSorted( Sq.begin( ), Sq.end( ) );

  // Sort
  auto start = std::chrono::high_resolution_clock::now( );
  BubbleSort( Sb.begin( ), Sb.end( ) );
  auto end = std::chrono::high_resolution_clock::now( );
  double tb =  
    std::chrono::duration_cast< std::chrono::nanoseconds >( end - start ).
    count( );
  tb *= 10e-10;

  start = std::chrono::high_resolution_clock::now( );
  InsertionSort( Si.begin( ), Si.end( ) );
  end = std::chrono::high_resolution_clock::now( );
  double ti =  
    std::chrono::duration_cast< std::chrono::nanoseconds >( end - start ).
    count( );
  ti *= 10e-10;

  start = std::chrono::high_resolution_clock::now( );
  QuickSort( Sq.begin( ), Sq.end( ) );
  end = std::chrono::high_resolution_clock::now( );
  double tq =  
    std::chrono::duration_cast< std::chrono::nanoseconds >( end - start ).
    count( );
  tq *= 10e-10;

  // Show results
  std::cout
    << "Bubble    : " << tb << "\t("
    << IsSorted( Sb.begin( ), Sb.end( ) ) << ")\t(" << ib << ")" << std::endl;
  std::cout
    << "Insertion : " << ti << "\t("
    << IsSorted( Si.begin( ), Si.end( ) ) << ")\t(" << ii << ")" << std::endl;
  std::cout
    << "QuickSort : " << tq << "\t("
    << IsSorted( Sq.begin( ), Sq.end( ) ) << ")\t(" << iq << ")" << std::endl;

  // Save results
  std::ofstream ofile( "cxx_bubble.txt" );
  for( int v: Sb )
    ofile << v << std::endl;
  ofile.close( );

  ofile.open( "cxx_insertion.txt" );
  for( int v: Si )
    ofile << v << std::endl;
  ofile.close( );

  ofile.open( "cxx_quick.txt" );
  for( int v: Sq )
    ofile << v << std::endl;
  ofile.close( );

  return( 0 );
}

// eof - cxx_Experiments.cxx

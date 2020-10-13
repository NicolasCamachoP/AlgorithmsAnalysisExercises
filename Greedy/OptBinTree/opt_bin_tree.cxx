// Compilation: g++ -std=c++17 opt_bin_tree.cxx
// Use: ./a.out <file.txt>

#include <algorithm>
#include <cctype>
#include <fstream>
#include <iostream>
#include <map>
#include <limits>
#include <sstream>
#include <string>
#include <vector>
#include <boost/algorithm/string.hpp>

// ------------------------------------------------------------------------
double BestTreeNaive_Aux(
        const std::vector<double> &P,
        const std::vector<double> &Q,
        unsigned int i, unsigned int j
) {
    if (j == i - 1)
        return (Q[i - 1]);
    else {
        double q = std::numeric_limits<double>::max();
        for (unsigned int r = i; r <= j; ++r) {
            double v = BestTreeNaive_Aux(P, Q, i, r - 1);
            v += BestTreeNaive_Aux(P, Q, r + 1, j);
            for (unsigned int l = i; l <= j; ++l)
                v += P[l - 1];
            for (unsigned int l = i - 1; l <= j; ++l)
                v += Q[l];
            if (v < q) {
                q = v;
            } // end if
        } // end for
        return (q);
    } // end if
}

// ------------------------------------------------------------------------
double BestTreeMem_Aux(
        const std::vector<double> &P,
        const std::vector<double> &Q,
        unsigned int i, unsigned int j,
        std::vector<std::vector<double> > &W,
        std::vector<std::vector<double> > &M
) {
    if (M[i][j] == std::numeric_limits<double>::max()) {
        //std::cout << "Toca entrar " << "i: " << i << " j: " << j << std::endl;
        if (j == i - 1)
            M[i][j] = Q[i - 1];
        else if (i<=j){
            double q = std::numeric_limits<double>::max();
            for (unsigned int r = i; r <= j; ++r) {
                double v = BestTreeMem_Aux(P, Q, i, r - 1, W, M);
                v += BestTreeMem_Aux(P, Q, r + 1, j, W, M);
                v += W[i - 1][j - 1];
                if (v < M[i][j]) {
                    M[i][j] = v;
                } // end if
            } // end for
        } // end if
    }// end if
    return M[i][j];
}

// ------------------------------------------------------------------------
double BestTreeNaive(const std::vector<double> &P, const std::vector<double> &Q) {
    return (BestTreeNaive_Aux(P, Q, 1, P.size()));
}

// ------------------------------------------------------------------------
double BestTreeMem(const std::vector<double> &P, const std::vector<double> &Q) {
    std::vector<std::vector<double> > W(P.size() , std::vector<double>(P.size() , 0));
    std::vector<std::vector<double> > M(P.size() + 2, std::vector<double>(P.size() + 2, 0));
    M[P.size()][P.size()] = std::numeric_limits<double>::max();
    M[P.size()][P.size() - 1] = Q[P.size() - 1];
    W[P.size() - 1][P.size() - 1] = Q[P.size() - 1] + Q[P.size()] + P[P.size() - 1];
    for (unsigned int i = 1; i < P.size(); i++) {
        W[i - 1][i - 1] = Q[i - 1] + P[i - 1] + Q[i];
        M[i][i - 1] = Q[i - 1];
        for (unsigned int j = i + 1; j <= P.size() + 1; j++) {
            W[i - 1][j - 1] = W[i - 1][j - 2] + P[j - 1] + Q[j];
            M[i][j - 1] = std::numeric_limits<double>::max();
        }// end for
    }// end for
    //std::cout<< M[1][P.size()]<<std::endl;



    /*std::cout<<"W"<<std::endl;
    for (unsigned int i = 0; i < P.size(); i++){
        for (unsigned int j = 0; j < P.size(); j++){
            std::cout<<W[i][j]<<" ";
        }
        std::cout<<std::endl;
    }
    std::cout<<"------------------------------------------------------"<<std::endl;
    for (unsigned int i = 0; i <= P.size(); i++){
        for (unsigned int j = 0; j <= P.size(); j++){
            std::cout<<M[i][j]<<" ";
        }
        std::cout<<std::endl;
    }*/
    return (BestTreeMem_Aux(P, Q, 1, P.size(), W, M) + Q[P.size()]);

    //return 0;
}
// ------------------------------------------------------------------------
std::vector<std::vector<double>> BestTreeBUP( const std::vector< double >& P, const std::vector< double >&  Q )
{
    std::vector<std::vector<double>> W ( P.size( ), std::vector<double> ( P.size( ), 0 ) );
    std::vector<std::vector<double>> M ( P.size( ) + 3, std::vector<double> ( P.size( ) + 3, 0 ) );
    std::vector<std::vector<double>> R ( P.size( ), std::vector<double> ( P.size( ) , 0 ) );
    for( unsigned int i = 1; i < P.size( ); i++ )
    {
        W[ i - 1 ][ i - 1 ] = Q[ i - 1 ] + P[ i - 1 ] + Q[ i ];
        M[ i ][ i - 1 ] = Q[ i - 1 ];
        for( unsigned int j = i + 1; j <= P.size( ); j++ )
        {
            W[ i - 1 ][ j - 1 ] = W[ i - 1 ][ j - 2 ] + P[ j - 1 ] + Q[ j ];
            M[ i ][ j - 1 ] = std::numeric_limits< double >::max( );
        }// end for
    }// end for
    M[P.size()][P.size()] = std::numeric_limits<double>::max();
    M[P.size()][P.size() - 1] = Q[P.size() - 1];
    W[P.size() - 1][P.size() - 1] = Q[P.size() - 1] + Q[P.size()] + P[P.size() - 1];
    for( unsigned int l = 1 ; l < P.size( ); l++ )
    {
        for( unsigned int i = 1; i < P.size( ); i++ )
        {
            int j = i + l - 1;
            for( int r = i; r < j; r++)
            {
                double v = M[ i ][ r - 1 ];
                v       += M[ r + 1 ][ j ];
                v += W[ i - 1 ][ j - 1 ];
                if( v < M[ i ][ j ] )
                {
                    M[ i ][ j ] = v;
                    R[ i ][ j ] = r;
                } // end if

            }//end for
        }//end for
    }// end for
    return R;
}


// ------------------------------------------------------------------------
int main(int argc, char **argv) {
    // Read file into a string
    /*std::ifstream input( argv[ 1 ] );
    std::stringstream strbuffer;
    strbuffer << input.rdbuf( );
    input.close( );
    std::string buffer = strbuffer.str( );

    // Tokenize string
    std::vector< std::string > tokens;
    boost::algorithm::split(
      tokens, buffer,
      boost::is_any_of( " ,.:;\"\'¿?¡!\n\t()" )
      );

    // Build histogram
    std::map< std::string, double > histogram;
    double off = double( 1 ) / double( tokens.size( ) );
    for( std::string& token: tokens )
    {
      std::transform(
        token.begin( ), token.end( ), token.begin( ),
        []( char c )
        {
          return( std::tolower( c ) );
        }
        );
      histogram[ token ] += off;
    } // end for

    double sProb = 0.8;
    double fProb = 1.0 - sProb;
    unsigned long qSize = histogram.size( ) + 1;
    std::vector< double > P, Q( qSize, fProb / double( qSize ) );
    for( const auto& b: histogram )
      P.push_back( b.second * sProb );
    */
    //TODO
    std::vector<double> P;
    P.push_back(0.15);
    P.push_back(0.1);
    P.push_back(0.05);
    P.push_back(0.1);
    P.push_back(0.2);

    std::vector<double> Q;
    Q.push_back(0.05);
    Q.push_back(0.1);
    Q.push_back(0.05);
    Q.push_back(0.05);
    Q.push_back(0.05);
    Q.push_back(0.1);

    //std::cout << BestTreeNaive(P, Q) << std::endl;
    //std::cout << BestTreeMem(P, Q) << std::endl;
    auto a =BestTreeBUP(P, Q);
    for (unsigned int i = 0; i < P.size(); i++){
        for (unsigned int j = 0; j < P.size(); j++){
            std::cout<<a[i][j]<<" ";
        }
        std::cout<<std::endl;
    }

    return (0);
}
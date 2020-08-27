#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <time.h>
#include <string.h>


#define MAX_THREADS 4

int color = 0;
int col = 0;

struct ThreadData {
    int *Matrix;
    int x;
    int y;
    int k;
};

void *FillMatrix(struct ThreadData *ptr) {
    int i;
    int j;
    int *mat = ptr->Matrix;
    for ( i = ptr->y; i < ptr->k + ptr->y; i++ ) {
        for ( j = ptr->x; j < ptr->k + ptr->x; j++ ) {
            *(mat + i * col + j) = 0;
        }
    }
    pthread_exit((void *) 0);
}

void PrintMatrix(const int *mat, int k) {
    FILE *fptr;
    int i;
    int j;

    fptr = fopen("output.txt", "w+");
    for ( i = 0; i < k; i++ ) {
        for ( j = 0; j < k; j++ ) {
            fprintf(fptr, "%d ", *(mat + i * k + j));
        }
        fprintf(fptr, "\n");
    }
}

void OutMatrix(const int *mat, int k) {
    int i;
    int j;

    for ( i = 0; i < k; i++ ) {
        for ( j = 0; j < k; j++ ) {
            printf("%d ", *(mat + i * k + j));
        }
        printf("\n");
    }
}

void Color(int *mat, int x1, int y1, int x2, int y2, int x3, int y3) {
    color++;
    *(mat + y1 * col + x1) = color;
    *(mat + y2 * col + x2) = color;
    *(mat + y3 * col + x3) = color;
}

int Sector(int *mat, int n, int x, int y, int r, int c) {
    int x0, y0, x1, y1, x2, y2, x3, y3, newSize;
    if ( n == 2 ) {
        color++;
        for ( int i = 0; i < n; i++ ) {
            for ( int j = 0; j < n; j++ ) {
                if ( *(mat + (y + j) * col + (x + i)) == 0 ) {
                    *(mat + (y + j) * col + (x + i)) = color;
                }
            }
        }
        return 0;
    }
    newSize = n >> 1;
    // Checking the first quadrant
    if ( r < y + newSize && c < x + newSize ) {
        x0 = c;
        y0 = r;
        x1 = x + newSize;
        y1 = y + (newSize) - 1;
        x2 = x1 - 1;
        y2 = y1 + 1;
        x3 = x1;
        y3 = y2;
        Color(mat, x1, y1, x2, y2, x3, y3);
    }
        // Checking the second quadrant
    else if ( r < y + newSize && c >= x + newSize ) {
        x1 = c;
        y1 = r;
        x0 = x + newSize - 1;
        y0 = y + (newSize) - 1;
        x2 = x0;
        y2 = y0 + 1;
        x3 = x2 + 1;
        y3 = y2;
        Color(mat, x0, y0, x2, y2, x3, y3);
    }
        // Checking the third quadrant
    else if ( r >= y + newSize && c < x + newSize ) {
        x2 = c;
        y2 = r;
        x1 = x + newSize;
        y1 = y + (newSize) - 1;
        x0 = x1 - 1;
        y0 = y1;
        x3 = x1;
        y3 = y1 + 1;
        Color(mat, x0, y0, x1, y1, x3, y3);
    }
        // Checking the fourth quadrant
    else if ( r >= y + newSize && c >= x + newSize ) {
        x3 = c;
        y3 = r;
        x1 = x + newSize;
        y1 = y + (newSize) - 1;
        x2 = x1 - 1;
        y2 = y1 + 1;
        x0 = x2;
        y0 = y1;
        Color(mat, x0, y0, x1, y1, x2, y2);
    }
    // First
    Sector(mat, newSize, x, y, y0, x0);
    // Second
    Sector(mat, newSize, x + newSize, y, y1, x1);
    // Third
    Sector(mat, newSize, x, y + newSize, y2, x2);
    // Fourth
    Sector(mat, newSize, x + newSize, y + newSize, y3, x3);

    return 0;
}

int main(int argc, char **argv) {
    char flag = 0;
    if ( argc < 4 || argc > 5 ) {
        printf("Usage: fasterboy [k] [i] [j] (-o) : file output (-t) : terminal output");
        exit(-1);
    }
    if ( argc == 5 ) {
        if ( strcmp(argv[ 4 ], "-o") == 0 )
            flag = 1;
    }
    clock_t time;
    int i = 0;
    pthread_t threads[MAX_THREADS];
    struct ThreadData thread_data[MAX_THREADS];
    int k = 1 << atoi(argv[ 1 ]);
    col = k;
    int x = atoi(argv[ 2 ]);
    int y = atoi(argv[ 3 ]);
    int *mat = (int *) malloc(k * k * sizeof(int));

    thread_data[ 0 ].x = 0;
    thread_data[ 0 ].y = 0;
    thread_data[ 0 ].k = k >> 1;
    thread_data[ 0 ].Matrix = mat;

    thread_data[ 1 ].x = 0;
    thread_data[ 1 ].y = thread_data[ 0 ].k;
    thread_data[ 1 ].k = thread_data[ 0 ].k;
    thread_data[ 1 ].Matrix = mat;

    thread_data[ 2 ].x = thread_data[ 0 ].k;
    thread_data[ 2 ].y = 0;
    thread_data[ 2 ].k = thread_data[ 0 ].k;
    thread_data[ 2 ].Matrix = mat;

    thread_data[ 3 ].x = thread_data[ 0 ].k;
    thread_data[ 3 ].y = thread_data[ 0 ].k;
    thread_data[ 3 ].k = thread_data[ 0 ].k;
    thread_data[ 3 ].Matrix = mat;

    time = clock();
    for ( ; i < MAX_THREADS; i++ ) {
        pthread_create(&threads[ i ], NULL, (void *) FillMatrix, &thread_data[ i ]);
    }
    for ( i = 0; i < MAX_THREADS; i++ ) {
        pthread_join(threads[ i ], NULL);
    }

    *(mat + y * k + x) = -1;

    Sector(mat, k, 0, 0, y, x);
    time = clock() - time;
    if ( flag == 1 ) {
        printf("Using File Output...\n");
        PrintMatrix(mat, col);
    } else {
        printf("Using Terminal Output...\n");
        OutMatrix(mat, col);
    }
    double time_taken = ((double) time) / CLOCKS_PER_SEC;
    printf("Filling the matrix took %f seconds.\n", time_taken);
    free(mat);
}

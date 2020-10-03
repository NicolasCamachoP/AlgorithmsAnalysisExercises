all: c_Experiments cxx_Experiments

c_Experiments: c_Experiments.c c/BubbleSort.c c/InsertionSort.c c/QuickSort.c c/IsSorted.c c/SortFunctions.h
	gcc c_Experiments.c c/BubbleSort.c c/InsertionSort.c c/QuickSort.c c/IsSorted.c -o c_Experiments

cxx_Experiments: cxx_Experiments.cxx cxx/BubbleSort.hxx cxx/InsertionSort.hxx cxx/QuickSort.hxx cxx/IsSorted.hxx cxx/SortFunctions.h
	g++ -std=c++17 cxx_Experiments.cxx -o cxx_Experiments

## eof - Makefile
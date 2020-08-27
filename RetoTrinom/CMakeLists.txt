cmake_minimum_required(VERSION 3.0)
set(CMAKE_C_COMPILER "gcc")
project(fasterboy C)

set(CMAKE_C_STANDARD 11)
set(THREADS_PREFER_PTHREAD_FLAG ON)
SET(GCC_COVERAGE_COMPILE_FLAGS "-march=native -O3 -pipe")
add_definitions(${GCC_COVERAGE_COMPILE_FLAGS})

find_package(Threads REQUIRED)

add_executable(fasterboy Faster.c)

target_link_libraries(fasterboy PRIVATE Threads::Threads)

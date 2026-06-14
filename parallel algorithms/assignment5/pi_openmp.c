// Wonjun Jo

#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>
#include <inttypes.h>
#include <omp.h>

uint64_t n = 1000000; // number of terms to use
int numThreads = 10; // number of threads to use

long double partialSum(int rank, uint64_t block) {
    long double partial = 0;
    for (uint64_t i = rank*block; i < (rank+1)*block; i++) {
        double sign = (double) (i%2==0 ? 1: -1); 
        partial += sign/(2*i+1);
    }
    return partial;
}

int main(int argc, char** argv) {

    char* endptr;
    if (argc == 2) { // if n is inputted but not threads
    	n = strtoull(argv[1], &endptr, 10);
    } else if (argc > 2) { // if both arguments are inputted
    	n = strtoull(argv[1], &endptr, 10);
    	numThreads = atoi(argv[2]);
    }
    double startTime = omp_get_wtime();
    
    uint64_t block = n/numThreads; // number of terms computed per thread
    
    long double sum = 0;
    
    #pragma omp parallel num_threads(numThreads) reduction(+: sum) 
    {
    	int rank = omp_get_thread_num();
    	sum += partialSum(rank, block);
    }
    
    sum *= 4;
    
    double endTime = omp_get_wtime();

    printf("Pi is %.20Lf\n", sum);    
    printf("We used %ld terms\n", n);
    printf("The time taken is %f \n", endTime - startTime);
    
    return 0;
}






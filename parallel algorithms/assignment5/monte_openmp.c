// Wonjun Jo

#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>
#include <math.h>
#include <inttypes.h>
#include <omp.h>

uint64_t n = 1000000; // number of samples to use
int numThreads = 10; // number of threads to use

uint64_t partialSample(int rank, uint64_t block) {
    srand(time(NULL)+rank); // ensure each thread has unique random seed
    uint64_t inside = 0; // number of points inside circle
    
    for (uint64_t i = rank*block; i < (rank+1)*block; i++) {
    	long double x = ((long double) rand())/RAND_MAX; // random x coordinate in [0,1]
    	long double y = ((long double) rand())/RAND_MAX; // random y coordinate in [0,1]
    	if (x*x + y*y <= 1) { // if in the circle
    	    inside++;
    	}
    }

    return inside; 
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
    uint64_t countIn = 0; // counts the cumulative number of points inside circle
        
    #pragma omp parallel num_threads(numThreads) reduction(+: countIn) 
    {
    	int rank = omp_get_thread_num();
    	countIn += partialSample(rank, block);
    }
    
    long double Pi = ((long double) countIn)/n;
    Pi *= 4;
    
    double endTime = omp_get_wtime();
    
    printf("Pi is %.20Lf\n", Pi);    
    printf("We used %ld samples\n", n);
    printf("The time taken is %f \n", endTime - startTime);
    
    return 0;
}






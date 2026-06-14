// Wonjun Jo

#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>
#include <math.h>
#include <pthread.h>
#include <inttypes.h>

int n = 1000000; // number of terms to use
int numThreads = 10; // number of threads to use

void* find_pi(void* ID) {

    uintptr_t id = (uintptr_t) ID; // the ID or rank of the thread
    int64_t block = n/numThreads; // number of items to add per thread
    long double* ans = malloc(sizeof(long double)); // the sum of one thread block
    
    for (int64_t i = block*id; i < block*(id+1); i++) {
    	*ans += pow(-1,i)/(2*i+1);
    }

    return (void*) ans; 
}

int main(int argc, char** argv) {

    if (argc == 2) { // if n is inputted but not threads
    	n = atoi(argv[1]);
    } else if (argc > 2) { // if both arguments are inputted
    	n = atoi(argv[1]);
    	numThreads = atoi(argv[2]);
    }
    
    struct timespec start, end; //structs used for timing purposes, it has two memebers, a tv_sec which is the current second, and the tv_nsec which is the current nanosecond.
    double time_diff;
    clock_gettime(CLOCK_MONOTONIC, &start); //Start the clock!
    //long double pi = find_pi(n);
    
    pthread_t* handlers = malloc(numThreads*sizeof(pthread_t));
    uintptr_t i = 0;
    for (i = 0; i < numThreads; i++) {
    	pthread_create(&handlers[i], NULL, find_pi, (void*) i);
    }
    
    long double sum = 0;
    long double* ret_val;
    for (i = 0; i < numThreads; i++) {
    	pthread_join(handlers[i], (void**) &ret_val);
    	sum += *ret_val;
    	free(ret_val);
    }

    sum *= 4;
    
    clock_gettime(CLOCK_MONOTONIC, &end);   //Stops the clock!
    free(handlers); // free the memory

    time_diff = (end.tv_sec - start.tv_sec); //Difference in seconds
    time_diff += (end.tv_nsec - start.tv_nsec) / 1e9; //Difference in nanoseconds

    printf("The time taken is %f \n", time_diff);
    printf("We used %d terms\n", n);
    printf("We used %d threads\n", numThreads);
    printf("Pi is %.20Lf\n", sum);
    
    return 0;
}






// Wonjun Jo

#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>
#include <math.h>

// n is the number of terms in the series to calculate Pi
long double find_pi(int n) {
    long double Pi = 0;
    
    for (int i = 0; i < n; i++) {
    	Pi += pow(-1,i)/(2*i+1);
    }
    
    Pi *= 4;
    return Pi; 
}

int main(int argc, char** argv) {
    int n;
    if (argc <= 1) {
    	n = 1000000;
    } else {
    	n = atoi(argv[1]);
    }

    struct timespec start, end; //structs used for timing purposes, it has two memebers, a tv_sec which is the current second, and the tv_nsec which is the current nanosecond.
    double time_diff;

    clock_gettime(CLOCK_MONOTONIC, &start); //Start the clock!
    long double pi = find_pi(n);
    clock_gettime(CLOCK_MONOTONIC, &end);   //Stops the clock!

    time_diff = (end.tv_sec - start.tv_sec); //Difference in seconds
    time_diff += (end.tv_nsec - start.tv_nsec) / 1e9; //Difference in nanoseconds

    printf("The time taken is %f \n", time_diff);
    printf("We used %d terms\n", n);
    printf("Pi is %.20Lf\n", pi);
    
    return 0;
}






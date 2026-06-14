
// Wonjun Jo

#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>
#include <math.h>

// n is the number of samples we use
long double find_pi(int n) {
    int in = 0; // number of points inside the circle (border included)
    for (int i = 0; i < n; i++) { // we are simplifying by only sampling 1 quadrant (still pi/4)
    	long double x = ((long double) rand())/RAND_MAX; // random x coordinate in [0,1]
    	long double y = ((long double) rand())/RAND_MAX; // random y coordinate in [0,1]
    	if (pow(x,2) + pow(y,2) <= 1) { // if in the circle
    	    in++;
    	}
    }
    long double Pi = ((long double) in)/n; // ratio of points in circle and total
    Pi *= 4;
    
    return Pi; 
}


int main(int argc, char** argv) {
    srand(time(NULL));
    
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
    printf("We used %d samples\n", n);
    printf("Pi is %.20Lf\n", pi);
    
    return 0;
}






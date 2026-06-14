#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <inttypes.h>
#include <omp.h>
#define BUFFER 256

void swap(int64_t*, int64_t*);

/*
This function returns a pointer to an array with all the numbers in the file as int64_t
Sets *size to be the number of numbers
*/
int64_t* Populate(char* fname, uint64_t* size){
    FILE* fptr;
    fptr = fopen(fname, "r");
    char buffer[BUFFER];
    
    // first fgets call used to determine size
    fgets(buffer, BUFFER, fptr);
    *size = atoi(buffer);
    
    int64_t* arr = (int64_t*) malloc((*size) * 8);
    
    // dummy fgets calls to move cursor to actual first input
    fgets(buffer, BUFFER, fptr);
    
    // now read each line of input into array
    for (uint64_t i = 0; i < *size; i++) {
        fgets(buffer, BUFFER, fptr);
        *(arr+i) = atoi(buffer);
    }
    
    return arr;
}

// implements odd/even sort
int my_sort(int64_t* input, uint64_t size) {
    
    for (uint64_t n = 0; n < size; n++) {
        #pragma omp parallel for
        for (uint64_t i = n%2; i < size-1; i += 2) {
            if (*(input+i) > *(input+i+1)) {
                swap(input+i, input+i+1);
            }
        }
    }
    
    return 0;
}

void swap(int64_t* x, int64_t* y) {
    int64_t temp;
    temp = *x;
    *x = *y;
    *y = temp;
}

/*
Suggested function to write, to check whether the array is sorted
Returns 0 if not sorted, returns 1 if sorted
*/
int is_sorted(int64_t* input, uint64_t size){
    
    for (uint64_t i = 0; i < size-1; i++) {
        if (*(input+i) > *(input+i+1)) {
            return 0;
        }
    }
    return 1;
}

int main(int argc, char** argv) {
    uint64_t n; //The input size
    int64_t* input = Populate("./numbers.txt", &n); //gets the array

    double startTime = omp_get_wtime();
    my_sort(input, n);
    double endTime = omp_get_wtime();
    
    //check if it's sorted.
    int sorted = is_sorted(input, n);

    printf("Are the numbers sorted? %s \n", sorted ? "true" : "false");
    printf("Time elapsed: %lf \n", endTime - startTime);
    free(input);
}





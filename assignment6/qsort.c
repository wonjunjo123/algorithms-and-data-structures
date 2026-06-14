#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <inttypes.h>
#include <omp.h>
#include <time.h>
#define BUFFER 256

void swap(int64_t*, int64_t*);
int print_array(int64_t*, int64_t);

/*
This function returns a pointer to an array with all the numbers in the file as int64_t
Sets *size to be the number of numbers
*/
int64_t* Populate(char* fname, int64_t* size) {
    FILE* fptr;
    fptr = fopen(fname, "r");
    char buffer[BUFFER];
    
    // first fgets call used to determine size
    fgets(buffer, BUFFER, fptr);
    *size = atoi(buffer);
    
    int64_t* arr = (int64_t*) malloc((*size) * 8);
    
    // dummy fgets calls to move cursor to actual first input
    fgets(buffer, BUFFER, fptr);
    
    for (int64_t i = 0; i < *size; i++) {
        fgets(buffer, BUFFER, fptr);
        *(arr+i) = atoi(buffer);
    }
    
    return arr;
}


/*
Partitions the array and returns the index of the pivot (after partition)
*/
int64_t partition(int64_t* input, int64_t left, int64_t right) {
    int64_t n = right - left + 1;
    int64_t pivot_index = rand()%n; // random index for pivot
    swap(input+left+pivot_index, input+right); // swap pivot to the end of list
    
    int64_t a = left-1; // index of last smaller-than-pivot element

    for (int64_t i = 0; i < n; i++) {
        if (*(input+left+i) < *(input+right)) { // if current element is smaller than pivot, 
            a++;
            swap(input+left+i, input+a);
        }
    }
    a++;
    swap(input+a, input+right); // swap pivot to where it should go

    pivot_index = a; // update the index at which pivot is now located

    return pivot_index;
}


/*
Sorts the input array and puts output back into the input array
*/
int my_qsort(int64_t* input, int64_t left, int64_t right) {

    if (left < right) {
        int64_t pivot_index = partition(input, left, right); // partition once and store pivot index
        
        //recursive to the left and right of pivot
        my_qsort(input, left, pivot_index-1);
        my_qsort(input, pivot_index+1, right);        
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
Returns 0 if not sorted, returns 1 if sorted
*/
int is_sorted(int64_t* input, int64_t size){
    for (int64_t i = 1; i < size; i++){
	if (input[i-1] > input[i]){
            return 0;
	}	
    }
    return 1;
}

int main(int argc, char** argv) {
    srand(time(NULL));
    int64_t n; //The input size
    int64_t* input = Populate("./numbers.txt", &n); //gets the array
    // Populate also sets n to a value by passing in address of n
    
    double startTime = omp_get_wtime();
    my_qsort(input, 0, n-1);
    double endTime = omp_get_wtime();

    //check if it's sorted.
    int sorted = is_sorted(input, n);
    
    printf("Are the numbers sorted? %s \n", sorted ? "true" : "false");
    printf("Time elapsed: %lf \n", endTime - startTime);
    free(input);
}






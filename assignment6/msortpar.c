

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <inttypes.h>
#include <omp.h>
#define BUFFER 256 // size of buffer that we want to read from
#define TASK_LIMIT 200 // array size limit for when we want to stop making tasks
// I played around with LIMIT but it seemed like 200 seemed to be relatively optimal
#define SIZE_LIMIT 1000 // input size limit for when we want to run things in parallel

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
    
    for (uint64_t i = 0; i < *size; i++) {
        fgets(buffer, BUFFER, fptr);
        *(arr+i) = atoi(buffer);
    }
    
    return arr;
}

int merge(int64_t* input, int64_t* temp, uint64_t left, uint64_t mid, uint64_t right) {

    uint64_t n1 = mid - left + 1; // length of the left portion of array
    uint64_t n2 = right - mid; // length of the left portion of array
    
    for (uint64_t i = 0; i < n1; i++) {
        *(temp+left+i) = *(input+left+i); // copy left portion of array to left portion of temp
    }
    for (uint64_t j = 0; j < n2; j++) {
        *(temp+mid+1+j) = *(input+mid+1+j); // copy left portion of array to left portion of temp
    }
    // Now it's as if we have "2" separate arrays (but we really just have one temp array)
    
    uint64_t i = 0; // index to keep track of left portion
    uint64_t j = 0; // index to keep track of right portion
    uint64_t k = left; // index to keep track of where we store it back into input
    
    // snake-like iteration over the left and right portions simultaneously
    while (i < n1 && j < n2) {
        if (*(temp+left+i) <= *(temp+mid+1+j)) {
            *(input+k) = *(temp+left+i); // push it back into input
            i++;
        } else {
            *(input+k) = *(temp+mid+1+j);
            j++;
        }
        k++;
    }
    
    while (i < n1) { // if there are any remaining in left portion, push the rest into input
        *(input+k) = *(temp+left+i);
        i++;
        k++;
    }
    
    while (j < n2) { // if there are any remaining in right portion, push the rest into input
        *(input+k) = *(temp+mid+1+j);
        j++;
        k++;
    }
    return 0;
    
}

/*
Helper for msort
*/
int my_msort_helper(int64_t* input, int64_t* temp, uint64_t size, uint64_t left, uint64_t right) {
    
    if (left < right) { // if the array length > 1
        uint64_t mid = left + (right - left)/2;
        
        // The idea here is that we only run tasks if initial sample size > SIZE_LIMIT
        // and even if that's the case, we stop making tasks once the recursive call's 
        // "array size" is less than TASK_LIMIT
        #pragma omp task shared(input, temp) firstprivate(left, mid) if(size > SIZE_LIMIT) final(mid-left < TASK_LIMIT)
        my_msort_helper(input, temp, size, left, mid);
        #pragma omp task shared(input, temp) firstprivate(mid, right) if(size > SIZE_LIMIT) final(right-mid < TASK_LIMIT)
        my_msort_helper(input, temp, size, mid+1, right);
        
        #pragma omp taskwait
        merge(input, temp, left, mid, right);
    }
    // if array length == 1, then it can stay where it is

    return 0;
}

/*
Sorts the input array and puts output back into the input array
*/
int my_msort(int64_t* input, uint64_t size){
    // Only create 1 temporary array
    int64_t* temp = malloc(size * sizeof(int64_t));

    // only run in parallel is input is bigger than SIZE_LIMIT
    #pragma omp parallel if(size > SIZE_LIMIT)
    #pragma omp single
    my_msort_helper(input, temp, size, 0, size-1); // Calls helper
    
    free(temp);
    
    return 0;
}

/*
Suggested function to write, to check whether the array is sorted
Returns 0 if not sorted, returns 1 if sorted
*/
int is_sorted(int64_t* input, uint64_t size){
    for (uint64_t i = 1; i < size; i++){
	if (input[i-1] > input[i]){
	    return 0;
	}	
    }
    return 1;
}

int main(int argc, char** argv){
    uint64_t n; //The input size
    int64_t* input = Populate("./numbers.txt", &n); //gets the array

    double startTime = omp_get_wtime();
    my_msort(input, n);
    double endTime = omp_get_wtime();
    
    //check if it's sorted.
    int sorted = is_sorted(input, n);
 
    printf("Are the numbers sorted? %s \n", sorted ? "true" : "false");
    printf("Time elapsed: %lf \n", endTime - startTime);
    free(input);
}











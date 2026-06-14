
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <inttypes.h>
#include <omp.h>
#include <time.h>
#include <math.h>

#define BUFFER 256
#define TASK_LIMIT 200
#define SIZE_LIMIT 1000

void swap(int64_t*, int64_t*);

/*
This function returns a pointer to an array with all the numbers in the file as int64_t
Sets *size to be the number of numbers
*/
int64_t* Populate(char* fname, int64_t* size){
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
Computes the prefix sum of in, with size number of elements. Store the result into out.
Returns total sum
*/
int64_t psum_seq(int64_t* in, int64_t* out, int64_t size) {
    int64_t sum = 0;
    for (int64_t i = 0; i < size; i++){
        sum += *(in+i);
        *(out+i) = sum;
    }
    return sum;
}

/*
Partitions the array and returns the index of the pivot (after partition)
This one is the sequential version
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

// assume sizes of 2^k for k >= 0
// assume in has been copied to out for general cases
int64_t psum_reduce(int64_t* in, int64_t* out, int64_t left, int64_t right, int64_t exp) {
    
    int64_t n = right - left + 1; // length of current array window

    if ((int64_t) pow(2,exp) < n) {
        if (n == 1) {
            *(out+left) = *(in+left);
        } else {
            int64_t c = (int64_t) pow(2,exp);
            #pragma omp parallel for if(n > SIZE_LIMIT) schedule(static)
            for (int64_t i = 0; i < n/(2*c); i++) {
                *(out+left+ 2*c*i + 2*c - 1) += *(out+left+ 2*c*i + c - 1);
            }
            psum_reduce(in, out, left, right, exp+1);
        }
    }
    
    return 1;
}

// assume sizes of 2^k for k >= 0
// assume in has been copied to out for general cases
int64_t psum_expand(int64_t* in, int64_t* out, int64_t left, int64_t right, int64_t exp) {
    
    int64_t n = right - left + 1; // length of current array window

    if ((int64_t) pow(2,exp+1) < n) {
        if (n == 1) {
            *(out+left) = *(in+left);
        } else {
            int64_t c = (int64_t) (n/pow(2,exp+1));
            #pragma omp parallel for if(n > SIZE_LIMIT) schedule(static)
            for (int64_t i = 0; i < n/c; i++) {
                int64_t val = (i>0) ? *(out+left+ c*i - 1) : 0;
                *(out+left+ c*i + c/2 - 1) += val;
            }
            psum_expand(in, out, left, right, exp+1);
        }
    }
    
    return 1;
}

// only scans inputs that are of length 2^k for some integer k>=0
int64_t psum_2k_par(int64_t* in, int64_t* out, int64_t left, int64_t right) {

    psum_reduce(in, out, left, right, 0); // 0 is exp    
    psum_expand(in, out, left, right, 0); // 0 is exp
    
    return *(out+right); // the last value of the input array is the cumulative sum of entire array
}

// algorithm for parallel scan regardless of length
// first I find the largest power of two length less or equal to the length...
// then I only perform parallel scan on that portion
// I find the largest power of two length less or equal to the remaining portion's length
// I add that portion's cumulative sum to just the next portion's first element
// then perform parallel scan on just that next portion
// keep going until you hit end of entire array.
int64_t psum_par(int64_t* in, int64_t* out, int64_t size, int64_t left, int64_t right) {

    int64_t n = right - left + 1;
    
    #pragma omp parallel for if(n > SIZE_LIMIT) schedule(static)
    for (int64_t i = 0; i < n; i++) {
        *(out+left+i) = *(in+left+i);
    }
    
    if (n <= 1) { // eventually this base case will hit
        *(out+left) = *(in+left);
        return 0;
    } else {
        // find largest power of two <= n
        int64_t exp = 1;
        while (2*exp <= n) {
            exp *= 2;
        } // mind you that exp is the length so remember to do left + exp for absolute index
    
        // remember that left and right are inclusive indexes so we need -1
        int64_t last_val = psum_2k_par(in, out, left, left+exp-1);
        if (left+exp <= right) {
            *(in+left+exp) += last_val; // to the first element of next portion, add cumulative sum of previous portion
        }
        psum_par(in, out, size, left+exp, right); // recursive call until base case
    }
    
    return *(out+right);

}

/*
Partitions the array and returns the index of the pivot (after partition) in parallel
*/
int64_t partition_par(int64_t* input, int64_t* out, int64_t* aux, int64_t size, int64_t left, int64_t right) {
    
    int64_t n = right - left + 1; // length of array from left to right
    int64_t pivot_index = rand()%n; // random index for pivot
    swap(input+left+pivot_index, input+right); // swap pivot to the end of list
    
    #pragma omp parallel for if(n > SIZE_LIMIT) schedule(static)
    for (int64_t i = 0; i < n; i++) { // Making aux array
        *(aux+left+i) = (*(input+left+i) <= *(input+right)) ? 1 : 0;
    }
    // do scan with aux array
    int64_t bigger_index = psum_par(aux, aux, size, left, right);
    // bigger_index is the index at which we start pushing numbers bigger than pivot
    // we define psum_par to take in and out array parameters because in general we probably want both input and output
    // but in our case, we don't need the 0/1 aux array, we only need the prefix sum, so we can use
    // aux for both in and out
    
    int64_t prev; // the value of aux at previous index
    
    // we start for loop at i = 0 if first value of input was bigger than pivot
    // we start at i = 1 if first value of input was smaller than pivot, so value got pushed to out
    #pragma omp parallel for if(n > SIZE_LIMIT) schedule(static)
    for (int64_t i = 0; i < n; i++) { 
        // if we are on the 0th index, set prev to 0 ... otherwise, prev = previous element of aux
        prev = (i>0) ? *(aux+left+i-1) : 0;
        if (*(aux+left+i) != prev) { // if psum is different than previous psum
            *(out+left+ *(aux+left+i)-1) = *(input+left+i); // input at i gets mapped to index = aux at i - 1
        }
    }
    
    
    // ---------- INVERSE OPERATION ---------- //
    #pragma omp parallel for if(n > SIZE_LIMIT) schedule(static)
    for (int64_t i = 0; i < n; i++) { // make inverse aux array
        *(aux+left+i) = (*(input+left+i) <= *(input+right)) ? 0 : 1; 
    } // I guess we also could have just done a binary invert of the inital aux array
    
    psum_par(aux, aux, size, left, right);
    
    #pragma omp parallel for if(n > SIZE_LIMIT) schedule(static)
    for (int64_t i = 0; i < n; i++) { 
        prev = (i>0) ? *(aux+left+i-1) : 0;
        if (*(aux+left+i) != prev) { // if psum is different than previous psum
            *(out+left+bigger_index+ *(aux+left+i)-1) = *(input+left+i); // input at i gets mapped to index = aux at i - 1
        } // we need to start at bigger_index
    }
    
    #pragma omp parallel for if(n > SIZE_LIMIT) schedule(static)
    for (int64_t i = 0; i < n; i++) { // push the output back into the input
        *(input+left+i) = *(out+left+i);
    } // the way I have my code designed, I don't save to output, I use out like a temp array and push results back into input

    return bigger_index - 1; // this is the index of the pivot
}


/*
Helper for qsort
size will always refer to the total length of the initial array regardless how deep the recursive calls
*/
int64_t my_qsort_helper(int64_t* input, int64_t* out, int64_t* aux, int64_t size, int64_t left, int64_t right) {

    int64_t pivot_index;

    if (left < right) {
        if (right-left==1) { // if array is just size 2
            if (*(input+left) > *(input+right)) {
                swap(input+left, input+right); // swap elements if needed, and do nothing else if not
            }
        } else {
            pivot_index = partition_par(input, out, aux, size, left, right); // partition once and store pivot index
        
            //recursive to the left and right of pivot
            #pragma omp task shared(input,out,aux) firstprivate(size, left, pivot_index) if(right-left > SIZE_LIMIT) final(pivot_index < TASK_LIMIT)
            if (left < left+pivot_index-1) {
                my_qsort_helper(input, out, aux, size, left, left+pivot_index-1);
            }
            #pragma omp task shared(input,out,aux) firstprivate(size, left, right, pivot_index) if(right-left > SIZE_LIMIT) final(right-left-pivot_index < TASK_LIMIT)
            if (left+pivot_index+1 < right) {
                my_qsort_helper(input, out, aux, size, left+pivot_index+1, right);
            }
        }
    }
    return 0;
}

/*
Sorts the input array and puts output back into the input array
*/
int my_qsort(int64_t* input, int64_t size) {

    // malloc this only once
    int64_t* out = malloc(size * sizeof(int64_t));
    int64_t* aux = malloc(size * sizeof(int64_t));
    
    // only run in parallel is input is bigger than SIZE_LIMIT
    #pragma omp parallel if(size > SIZE_LIMIT)
    #pragma omp single
    my_qsort_helper(input, out, aux, size, 0, size-1);
    
    free(out);
    free(aux);

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
int64_t is_sorted(int64_t* input, int64_t size){
    for (int64_t i = 1; i < size; i++){
	if (input[i-1] > input[i]){
	    return 0;
	}	
    }
    return 1;
}

/*
Returns 0 if the prefix sums agree, returns 1 if they agree
*/
int test_psum(int64_t* input, int64_t size){
    int64_t* out_seq = malloc(size * sizeof(int64_t));
    int64_t* out_par = malloc(size * sizeof(int64_t));
    
    psum_seq(input, out_seq, size);
    psum_par(input, out_par, size, 0, size-1);\
       
    for (int64_t i = 0; i < size; i++) {
        if (out_seq[i]!=out_par[i]){
            printf("Something didn't match!\n");
            
            return 0; // Something doesn't match! Leaks memory a bit but okay.
        }
    }

    free(out_par);
    free(out_seq);
    return 1;
}

int main(int argc, char** argv){
    srand(time(NULL));
    int64_t n; //The input size
    int64_t* input = Populate("./numbers.txt", &n); //gets the array

    double startTime = omp_get_wtime();
    my_qsort(input, n);
    double endTime = omp_get_wtime();
    
    //check if it's sorted.
    int64_t sorted = is_sorted(input, n);
    
    printf("Are the numbers sorted? %s \n", sorted ? "true" : "false");
    printf("Time elapsed: %lf \n", endTime - startTime);
    
    // test psum_par
    test_psum(input, n);
    
    free(input);
}










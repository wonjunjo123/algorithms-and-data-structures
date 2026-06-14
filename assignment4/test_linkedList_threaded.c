#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <pthread.h>
#include <time.h>
#include "linkedlist.h"

// USED THIS COMPILER COMMAND!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
// gcc -Wall -pthread linkedlist.c test_linkedList_threaded.c -o testthreaded
// !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


int THREADCOUNT = 400;
int OPS = 2; //An even number!

int MoreTests();

void* DoSafeDeletes(void* head){
    int t = time(NULL) ^ pthread_self();
    srand(t);
    for (int i =0; i < OPS/2; i++){
        uint32_t loc = rand() % (OPS);
        SafeDelete(head, loc);
    }
    return NULL;
}

void* DoSafeInserts(void* head){
    int t = time(NULL) ^ pthread_self();
    srand(t);
    for (int i =0; i<OPS; i++){
        uint32_t val = rand() % (THREADCOUNT * OPS);
        uint32_t loc = rand() % (OPS);
        SafeInsert(head, val, loc);
    }
    return NULL;
}

// I ADDED THIS ONE FOR MORETESTS()
void* DoSafeFinds(void* head){
    int t = time(NULL) ^ pthread_self();
    srand(t);
    for (int i =0; i<OPS/2; i++){
        uint32_t val = rand() % (THREADCOUNT * OPS);
        void* target = SafeFind(head, val);
        if (target) {
            printf("%ld is in the list\n", (uint64_t) target);
        }
        else {
            printf("%ld is not in the list. That is wrong!\n", (uint64_t) target);
        }
    }
    return NULL;
}

void* DoDeletes(void* head){
    int t = time(NULL) ^ pthread_self();
    srand(t);
    for (int i =0; i < OPS/2; i++){
        uint32_t loc = rand() % (OPS);
        Delete(head, loc);
    }
    return NULL;
}
void* DoInserts(void* head){
    int t = time(NULL) ^ pthread_self();
    srand(t);
    for (int i =0; i<OPS; i++){
        uint32_t val = rand() % (THREADCOUNT * OPS);
        uint32_t loc = rand() % (OPS);
        Insert(head, val, loc);
    }
    return NULL;
}

int TestSafeInserts(void* head){
    pthread_t* handlers = malloc(sizeof(pthread_t)*THREADCOUNT);
    for (int i = 0; i< THREADCOUNT; i++){
        pthread_create(&handlers[i], NULL, DoSafeInserts, (void*) head);
    }
  
    for (int i = 0; i< THREADCOUNT; i++){
        pthread_join(handlers[i], NULL);
    }

    int length = Display(head);
    printf("There are %d numbers. There should be %d numbers. \n", length, THREADCOUNT * OPS);
    return 0;
}

int TestSafeDeletes(void* head, int target_numb){
    pthread_t* handlers = malloc(sizeof(pthread_t)*THREADCOUNT);
    for (int i = 0; i< THREADCOUNT; i++){
        pthread_create(&handlers[i], NULL, DoSafeDeletes, (void*) head);
    }
  
    for (int i = 0; i< THREADCOUNT; i++){
        pthread_join(handlers[i], NULL);
    }

    int length = Display(head);
    printf("There are %d numbers. There should be %d numbers. \n", length, target_numb);
    return 0;
}

// I ADDED THIS ONE FOR MORETESTS()
int TestSafeFinds(void* head){
    pthread_t* handlers = malloc(sizeof(pthread_t)*THREADCOUNT);
    for (int i = 0; i< THREADCOUNT; i++){
        pthread_create(&handlers[i], NULL, DoSafeFinds, (void*) head);
    }
  
    for (int i = 0; i< THREADCOUNT; i++){
        pthread_join(handlers[i], NULL);
    }

    return 0;
}

int TestUnsafeInserts(void* head){
    pthread_t* handlers = malloc(sizeof(pthread_t)*THREADCOUNT);
    for (int i = 0; i< THREADCOUNT; i++){
        pthread_create(&handlers[i], NULL, DoInserts, (void*) head);
    }
  
    for (int i = 0; i< THREADCOUNT; i++){
        pthread_join(handlers[i], NULL);
    }

    int length = Display(head);
    printf("There are %d numbers. There should be %d numbers. \n", length, THREADCOUNT * OPS);
    return 0;
}

int TestUnsafeDeletes(void* head, int target_numb){
    pthread_t* handlers = malloc(sizeof(pthread_t)*THREADCOUNT);
    for (int i = 0; i< THREADCOUNT; i++){
        pthread_create(&handlers[i], NULL, DoDeletes, (void*) head);
    }
  
    for (int i = 0; i< THREADCOUNT; i++){
        pthread_join(handlers[i], NULL);
    }

    int length = Display(head);
    printf("There are %d numbers. There should be %d numbers. \n", length, target_numb);
    return 0;
}



int main(int argc, char** argv){
    if (argc == 2){
        THREADCOUNT = strtoul(argv[1], NULL, 10);
    }

    printf("Safe tests!\n");
    //"Safe" tests
    void* head = Create();
    TestSafeInserts(head);
    TestSafeDeletes(head, THREADCOUNT * OPS/2);
    TestSafeDeletes(head, 0);
    Destroy(head);

    //"Unsafe" tests
    //These may cause crashes or other race-y things.
    printf("\n\nUnsafe tests!\n");
    head = Create();
    TestUnsafeInserts(head);
    TestUnsafeDeletes(head, THREADCOUNT * OPS/2);
    TestUnsafeDeletes(head, 0);
    Destroy(head);

    //MoreTests(); //There are always more!
    return 0;
}

int MoreTests(){
    void* head = Create();
    TestSafeInserts(head);
    // created TestSafeFinds
    TestSafeFinds(head);
    Destroy(head);
    return 0;
}






















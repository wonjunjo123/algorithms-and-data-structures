#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <pthread.h>

//This is a basic node of the linked list. You will need to change this line to create a proper doubly-linked list. And please name it something else!
struct Node {
    uint32_t val;
    struct Node* next;
    struct Node* previous;
};

struct List {
    struct Node* headNode;
    pthread_mutex_t lock;
};

//This function constructs and returns a pointer to the head of the linkedlist
//It should dynamically allocate a head and return a pointer to it
void* Create();

//Inserts an item of the value at the index loc. If loc is out-of-bounds, it should insert at the end of the list.
int Insert(void* head, uint32_t value, uint32_t loc); 

//These functions are not threadsafe
//Deletes the item at index loc. If loc is out-of-bounds, it should delete the last item in list.
int Delete(void* head, uint32_t loc);

//Finds whether a given item is in the list and returns a pointer to it!
void* Find(void* head, uint32_t value);

//These functions should be threadsafe
//Inserts an item of the value at the index loc. If loc is out-of-bounds, it should insert at the end of the list.
int SafeInsert(void* head, uint32_t value, uint32_t loc);

//Deletes the item at index loc. If loc is out-of-bounds, it should delete the last item in list.
int SafeDelete(void* head, uint32_t loc);

//Finds whether a given item is in the list and returns a pointer to it!
void* SafeFind(void* head, uint32_t value);



//These function do not need to be threadsafe
//This function should display a representation of the list and return the length of the list.
int Display(void* head); 

// This should free up the memory used by the list.
// Be sure to destroy the lock! (once you implement it).
int Destroy(void* head); 


















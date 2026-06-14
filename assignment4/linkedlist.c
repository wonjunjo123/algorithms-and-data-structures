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
#include "linkedlist.h"

//These functions should be threadsafe
//Inserts an item of the value at the index loc. If loc is out-of-bounds, it should insert at the end of the list.
int SafeInsert(void* head, uint32_t value, uint32_t loc) {
    struct List* list = (struct List*) head;
    pthread_mutex_lock(&(list->lock));
    
    struct Node* insertNode = (struct Node*) malloc(sizeof(struct Node));
    struct Node* currentNode = list->headNode; // the list's headNode node
    insertNode->val = value;
    
    int length = getLength(head);
    if (loc > length || loc < 0) { // if loc is out of bounds,
    	loc = length; // make it so that the insertion happens at the end
    }
    
    for (uint32_t i = 0; i <= loc; i++) {
        if (i == loc) {
            insertNode->next = currentNode->next;
            insertNode->previous = currentNode;
            if (currentNode->next != NULL) {
                currentNode->next->previous = insertNode;
            }
            currentNode->next = insertNode;

        } else {
            currentNode = currentNode->next;
        }
    }

    pthread_mutex_unlock(&(list->lock));
    return 1;
}


//Deletes the item at index loc. If loc is out-of-bounds, it should delete the last item in list.
int SafeDelete(void* head, uint32_t loc) {
    struct List* list = (struct List*) head;
    pthread_mutex_lock(&(list->lock));
    
    struct Node* currentNode = list->headNode;
    int length = getLength(head);
    if (length == 0) { // if there is nothing to remove
        return 0; // return 0
    }
    if (loc >= length || loc < 0) { // if loc is out of bounds, (in this case, >= not >)
    	loc = length-1; // make it so that the deleting happens at the end
    }
    
    currentNode = currentNode->next;
    for (uint32_t i = 0; i <= loc; i++) {
        if (i == loc) {
            currentNode->previous->next = currentNode->next;
            
            if (currentNode->next != NULL) {
                currentNode->next->previous = currentNode->previous;
            }
            free(currentNode); // free the memory of the node to be deleted
        } else {
            currentNode = currentNode->next;
        }
    }

    pthread_mutex_unlock(&(list->lock));
    return 1;
}


//Finds whether a given item is in the list and returns a pointer to it!
void* SafeFind(void* head, uint32_t value) {
    struct List* list = (struct List*) head;
    pthread_mutex_lock(&(list->lock));
    
    struct Node* currentNode = list->headNode;
    while (currentNode != NULL) {
        if (currentNode->val == value) {
            return currentNode;
        }
        currentNode = currentNode->next;
    }
    
    pthread_mutex_unlock(&(list->lock));
    return NULL;
}


//This function constructs and returns a pointer to the head of the linkedlist
//It should dynamically allocate a head and return a pointer to it
// WE ARE CREATING A LIST STRUCT THAT HAS A NODE STRUCT AND A LOCK
void* Create() {
    struct List* list = (struct List*) malloc(sizeof(struct List));
    list->headNode = (struct Node*) malloc(sizeof(struct Node));
    pthread_mutex_init(&(list->lock), NULL);
    list->headNode->val = NULL;
    list->headNode->next = NULL;
    list->headNode->previous = NULL;
    return list;
}


//These functions are not threadsafe
//Inserts an item of the value at the index loc. If loc is out-of-bounds, it should insert at the end of the list.
// parameter is misleading because head is actually a list struct that has a struct node which is a head
int Insert(void* head, uint32_t value, uint32_t loc) {

    struct List* list = (struct List*) head;
    struct Node* insertNode = (struct Node*) malloc(sizeof(struct Node));
    struct Node* currentNode = list->headNode; // the list's headNode node
    insertNode->val = value;
    
    int length = getLength(head);
    if (loc > length || loc < 0) { // if loc is out of bounds,
    	loc = length; // make it so that the insertion happens at the end
    }
    
    for (uint32_t i = 0; i <= loc; i++) {
        if (i == loc) {
            insertNode->next = currentNode->next;
            insertNode->previous = currentNode;
            if (currentNode->next != NULL) {
                currentNode->next->previous = insertNode;
            }
            currentNode->next = insertNode;

        } else {
            currentNode = currentNode->next;
        }
    }
    return 1;
}

// Deletes the item at index loc. If loc is out-of-bounds, it should delete the last item in list.
int Delete(void* head, uint32_t loc) {
    struct List* list = (struct List*) head;
    struct Node* currentNode = list->headNode;
    int length = getLength(head);
    if (length == 0) { // if there is nothing to remove
        return 0; // return 0
    }
    if (loc >= length || loc < 0) { // if loc is out of bounds, (in this case, >= not >)
    	loc = length-1; // make it so that the deleting happens at the end
    }
    
    currentNode = currentNode->next;
    for (uint32_t i = 0; i <= loc; i++) {
        if (i == loc) {
            currentNode->previous->next = currentNode->next;
            
            if (currentNode->next != NULL) {
                currentNode->next->previous = currentNode->previous;
            }
            free(currentNode); // free the memory of the node to be deleted
        } else {
            currentNode = currentNode->next;
        }
    }
    
    return 1;
    
}



//Finds whether a given item is in the list and returns a pointer to it!
void* Find(void* head, uint32_t value) {
    struct List* list = (struct List*) head;
    struct Node* currentNode = list->headNode;
    while (currentNode != NULL) {
        if (currentNode->val == value) {
            return currentNode;
        }
        currentNode = currentNode->next;
    }
    return NULL;
}



//These function do not need to be threadsafe
//This function should display a representation of the list and return the length of the list.
int Display(void* head) {
    int length = 0;
    struct List* list = (struct List*) head;
    struct Node* currentNode = list->headNode;
    currentNode = currentNode->next; // Moves to first node, if it exists
    while (currentNode != NULL) {
        printf("%d ", currentNode->val);
        length++;
        currentNode = currentNode->next;
    }
    printf("\n");
    
    return length;
}

//This should free up the memory used by the list. Be sure to destroy the lock! (once you implement it).
int Destroy(void* head) {
    struct List* list = (struct List*) head;
    pthread_mutex_destroy(&(list->lock));
    struct Node* currentNode = list->headNode;
    while (currentNode->next != NULL) {
        currentNode = currentNode->next;
        free(currentNode->previous);
    }
    free(currentNode);

    return 0;
}

// PERSONALLY DEFINED FUNCTIONS
// used to return length, differentiated from Display() because we don't want print output
int getLength(void* head) {
    int length = 0;
    struct List* list = (struct List*) head;
    struct Node* currentNode = list->headNode;
    currentNode = currentNode->next; // Moves to first node, if it exists
    while (currentNode != NULL) {
        length++;
        currentNode = currentNode->next;
    }
    return length;
}

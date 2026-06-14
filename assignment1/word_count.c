// Wonjun Jo

#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>
#define BUFFER_SIZE 200000

int isAlphabet(int n) {
    // returns 1 (true) if n is within the alphabet ASCII values of [65,90] or [97,122]
    if ((n>=65 && n<=90) || (n>=97 && n<=122)) return 1;
    else return 0; // false
}

int main(int argc, char** argv){

    FILE* file;
    char buffer[BUFFER_SIZE];
    int count = 0;
    char* target = "";
    
    if (argc > 2) {
        target = argv[2];
    }
    if (argc > 1) { // this is just for error handling for no additional input
    	file = fopen(argv[1], "r");
    } else { // default if no additional input
	file = fopen("declaration.txt", "r");
    }
    
    // store the entire file as a string into buffer
    fread(buffer, sizeof(buffer), 1, file);
    fclose(file);
    
    char* token = strtok(buffer, " ");
    int hasTarget = 0;
    int targetIndex = -1;

    while (token != NULL) {
        if (strlen(token) >= strlen(target)) {
            for (int i = 0; i <= strlen(token) - strlen(target); i++) {
                for (int j = 0; j < strlen(target); j++) {
                
                    // as soon as the sequence does not match,
                    // stop checking for this iteration
                    if (target[j] != tolower(token[i+j])) break;
                    
                    // if we make it to the last iteration,
                    // this means we have found the target sequence
                    if (j == strlen(target) - 1) {
                        hasTarget = 1;
                        targetIndex = i; // stores at which index target occurs
                    }
                }
            }
        }
        
        // this code is to avoid cases where target = "he" and token = "the","there","her"
        if (hasTarget == 1) {
            if (targetIndex == 0) { // if target begins at start of token,
                // and the character after target is an alphabet,
                // it means that it's not purely the word,
                if (isAlphabet(token[strlen(target)]) == 1) hasTarget = 0; // so don't count it
                
            } else if (targetIndex > 0) { // else if target begins in the middle of token,
                // and the character before OR after is an alphabet,
                if (isAlphabet(token[targetIndex - 1]) == 1 || \
                    isAlphabet(token[targetIndex + strlen(target)]) == 1) hasTarget = 0; // also don't count it
            }
        }
        
        // if after that filter, hasTarget == 1,
        // it means target was purely present as that word, so increment count
        if (hasTarget == 1) count++; 
        hasTarget = 0; // reset hasTarget for next iteration
        
        token = strtok(NULL, " "); // retrieve next token
        
    }
    
    printf("%s count: %d\n", target, count);
    
    return 0;
}





/*
Problem: In C or C++ write a function that reverses a null-terminated string
Solution: inc from start, dec from end. swap at each step
    - linear time, constant space

total time: 46

mistakes:
    - didn't deal with NULL edge case
struggles:
    - char*:
        - was passing "..." to function rather than setting to string and passing it
        - bus error because I was doing char* str = "..." instead of char str[] = "..."
    - printf: had to look up and slow to work with
    - NULL: had issues with NUL, NULL, '\0', forgot string literals had implicit '\0'
    - forgot about strlen so manually detemrined length of string
*/

#include <stdio.h>
#include <string.h>

void reverse(char* string) {
    if (!string) return;
    int i = 0, j = strlen(string) - 1;
    char temp;

    for(; i <= j; i++, j--) {
        temp = string[i];
        string[i] = string[j];
        string[j] = temp;
    }
}

int main() {
    char* string;
    strcpy(string, "abc");
    reverse(string);
    printf("%s\n", string);

    strcpy(string, "abcd");
    reverse(string);
    printf("%s\n", string);

    strcpy(string, "a");
    reverse(string);
    printf("%s\n", string);

    string = NULL;
    reverse(string);
    printf("%s\n", string);
    return 0;
}

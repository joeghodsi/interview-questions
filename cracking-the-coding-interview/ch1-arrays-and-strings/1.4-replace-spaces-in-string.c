/*
Problem: replace all spaces in a string with '%20'. May assume string has sufficient space. You are
    given true length of the string
Solution: maintain copy of original and iterate over it moving values into string based on an offset
    which is increased as spaces are found
    - linear time, linear space

total time: 40

mistakes:
    - didn't add null character to end of string after replacement
*/

#include <stdio.h>
#include <string.h>


void replace_spaces(char* str, int length) {
    char original_string[length];
    strcpy(original_string, str);
    int i = 0, offset = 0;
    for (i = 0; original_string[i] != '\0'; i++) {
        if (original_string[i] == ' ') {
            str[i+offset] = '%';
            str[i+offset+1] = '2';
            str[i+offset+2] = '0';
            offset += 2;
        } else {
            str[i+offset] = original_string[i];
        }
    }
    str[i+offset] = '\0';
}

int main() {
    char string[11] = "a b";
    replace_spaces(string, 11);
    printf("%s\n", string);

    strcpy(string, "a bc");
    replace_spaces(string, 11);
    printf("%s\n", string);

    strcpy(string, "a  bc");
    replace_spaces(string, 11);
    printf("%s\n", string);

    strcpy(string, "   a");
    replace_spaces(string, 11);
    printf("%s\n", string);
    return 0;
}

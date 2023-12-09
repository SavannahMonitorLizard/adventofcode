#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

#define MAX_LINE_LENGTH 256

void p1();
void p2();

int main() {
    
    p1();

    return 0;
}

void p1() {
    FILE *file = fopen("inputs\\p.txt", "r");
    char line[MAX_LINE_LENGTH];
    int total = 0;
    char buffer[20];
    char c1;
    char c2;
    char result[3];

    while (fgets(line, sizeof(line), file) != NULL) {
        for (int i = 0; line[i] != '\0'; i++) {
            if (isdigit(line[i])) {
                c1 = line[i];
                break;
            }
        }
        for (int i = strlen(line); i >= 0; i--) {
            if (isdigit(line[i])) {
                c2 = line[i];
                break;
            }
        }

        sprintf(result, "%c%c", c1, c2);
        total += atoi(result);
    }

    sprintf(buffer, "%i", total);
    printf("%s\n", buffer);

    fclose(file);
}

void p2() {

}
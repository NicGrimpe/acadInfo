#include "stdio.h"
#include "stdlib.h"
#include "limits.h"

typedef long long ultraLong; // 64 bits integer
ultraLong fast(unsigned int input) {
    return ((input*(input-1)) / 2);
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        printf("Needs an argument, max input is 2147483647!!!\n");
        return -1;
    }
    unsigned int input = (unsigned int) atoi(argv[1]);
    printf("Input --> %u\n", input);
    printf("--> %d\n", fast(input));
}
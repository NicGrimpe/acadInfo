#include "stdio.h"
#include "stdint.h"

typedef long long ultraLong; // 64 bits integer

ultraLong function(ultraLong input) {
    ultraLong out = 0;
    ultraLong i = 0;
    while(i < input) {
        out += i++;
    }
    return out;
}

ultraLong test_function(ultraLong input) {
    return ((input*(input-1)) / 2);
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        printf("Needs an argument!!!");
    }
    printf("--> %d\n", function(argv[1]));
}
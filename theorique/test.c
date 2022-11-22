#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

// Function address 0x555555555169
void hidden_function() {
  printf("Wait why are you here ???\n");
  exit(0);
}

int main(int argc, char **argv) {
    char buffer[8];
    volatile int (*fp)();

    fp = NULL;
    gets(buffer);

    if (fp) {
    printf("calling function pointer @ %p\n", fp);
    fp();
    }

    exit(0);
}
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
  struct {
    char buffer[8];
    volatile int (*fp)();
  } locals;

  locals.fp = NULL;
  gets(locals.buffer);

  if (locals.fp) {
    locals.fp();
  }

  exit(0);
}
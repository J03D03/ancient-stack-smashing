#include <stdio.h>

void reveal_secret() { printf("reveal_secret was executed\n"); }

int main() {
  int pin = 9999;
  char buffer[4];
  printf("Provide your input:\n");
  gets(buffer);
  if (pin == 42) { // We would like to pass this check
    reveal_secret();
  } else {
    printf("Try again.\n");
  }
}
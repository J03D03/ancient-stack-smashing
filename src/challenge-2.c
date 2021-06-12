#include <stdio.h>

void reveal_secret() { printf("Secret revealed\n"); }

int main() {
  int pin = 9999;
  char buffer[4];
  fprintf(stdout, "Provide your input:\n");
  gets(buffer);
  if (pin == 42) { // We would like to pass this check
    reveal_secret();
  } else {
    fprintf(stdout, "Try again.\n");
  }
}
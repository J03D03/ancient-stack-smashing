#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>
#include <unistd.h>

void reveal_secret() { printf("reveal_secret was executed\n"); }

void what_could_go_wrong() {
  char buffer[80];
  scanf("%[^\t]", buffer);
}

int main() {
  while (1) {
    if (fork() == 0) {
      // Child process
      what_could_go_wrong();
      return 0;
    } else {
      // Parent process
      int status;
      waitpid(-1, &status, 0);
    }
  }
}
#include "../src/my_code.h"

#include <stdlib.h>
#include <stdio.h>

int main(int argc, char **argv) {
  int a=atoi(argv[1]);
  int b=atoi(argv[2]);

  printf("%d\n", sum(a,b));
}

#include <stdio.h>

//CLIBRARYTEST is defined if test is called by callCFunction.
//Then, main-function is defined at tests/testmain.c
#ifndef CLIBRARYTEST
int main(int argc, char **argv) {
  printf("a b c\n");
}
#else
int sum(int a, int b) {
  return a+b;
}
#endif

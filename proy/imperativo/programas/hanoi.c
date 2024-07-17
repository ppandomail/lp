#include <stdio.h>
  #include <conio.h>
  void hanoi(int n,int com, int aux, int fin);
  void main(void) {
      hanoi(5, 'A', 'B', 'C');
  }
  void hanoi(int n,int com, int aux, int fin){
        if(n==1)
            printf("%c->%c",com,fin);
        else {
            hanoi(n-1,com,fin,aux);
            printf("\n%c->%c\n",com,fin);
            hanoi(n-1,aux,com,fin);
        }
  }
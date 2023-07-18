#include <stdio.h>
int main() {
    
     int rollNo[10];
     int i;
     printf("Enter the roll numbers(int) of 10 students (space sep):");
     for(i=0;i<10;i++) {
scanf("%d",&rollNo[i]);
     }
     printf("Roll numbers are:");
     for(i=0;i<10;i++) {
    printf("%d ",rollNo[i]);
      }
      return 0;
}

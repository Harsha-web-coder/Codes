#include <stdio.h>
int main() {
     int n;
     printf("Enter how many details of students should be stored:");
     scanf("%d",&n);
     int rollNo[n];
     
     for(int i=0;i<n;i++) {
         printf("Enter the roll numbers of student %d:",i+1);
         scanf("%d",&rollNo[i]);
     }
     printf("Roll numbers are:");
     for(int i=0;i<n;i++) {
    printf("%d ",rollNo[i]);
      }
      return 0;
}
#include <stdio.h>

int main () {
char grade;
printf("enter a grade in caps:");
scanf("%c",&grade);
   switch(grade) {
      case 'A' :
        printf("Excellent");
        break;
      case 'B' :
        printf("Good");
        break;
      case 'C' :
        printf("Average");
        break;
      case 'D' :
        printf("Below Average");
        break;
      case 'F' :
        printf("Fail");
        break;
      default :
        printf("The grade is invalid");
   }
   return 0;
}

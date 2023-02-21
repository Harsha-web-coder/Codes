#include<stdio.h>
#include<string.h>
struct Student{
char name[20];
float mark;
}StudentOne;
int main()
{
printf("enter name:");
scanf("%s",&StudentOne.name);
printf("enter marks:");
scanf("%f",&StudentOne.mark);
printf("your name is:%s\n",StudentOne.name);
printf("your marks:%.1f",StudentOne.mark);
return 0;
}
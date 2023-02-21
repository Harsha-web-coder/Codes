#include<stdio.h>
int main(){
int a;
printf("enter a number");
scanf("%d",&a);
switch(a){
case 0:
printf("you have entered 0");
return 0;
default:
    printf("you have entered other than 0");
}
}

/*
 
Enter lower and upper limits                                                                                                                  
1 50                                                                                                                                            
Prime numbers between 1 and 50 are :                                                                                                            
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47

*/

#include<stdio.h>
#include<stdlib.h>
int main()
{
    int num,flag,i,j,lower,upper;
    printf("Enter lower and upper limits\n");
    scanf("%d %d",&lower,&upper);
    printf("Prime numbers between %d and %d are :\n",lower,upper);
    for(i=lower+1;i<upper;i++)
    {
      flag=1;
     for(j=2;j<i;j++)
     {
        if(i%j==0)
         {
             flag=0;
             break;
          }
     }
     
    if(flag==1)
      printf("%d ",i);
     
  }    
    return 0; 
}


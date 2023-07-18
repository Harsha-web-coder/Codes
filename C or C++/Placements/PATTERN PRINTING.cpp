

/*  Enter the value of n                                                                                                  
5   
----------------
1                                                                                                                     
3*2                                                                                                                   
4*5*6                                                                                                                 
10*9*8*7                                                                                                              
11*12*13*14*15
----------------
*/

#include <stdio.h>

int main()
{
   int count=0,i,j,n;
   printf("Enter the value of n\n");
   scanf("%d",&n);
   for(i=1;i<=n;i++)
   {
       if(i%2!=0)
       {   for(j=1;j<=i;j++)
           {
            count++;
           if(j<i)
               printf("%d*",count);
           else
               printf("%d",count);
           }   
       }
       else
       {
           count=count+i;
           for(j=1;j<=i;j++)
           {
            
           if(j<i)
               printf("%d*",count);
           else
               printf("%d",count);
            count--;   
           }   
           count=count+i;
       }
       printf("\n");
   }
   
   
    return 0;
}




/*

Enter the number                                                                                                      
4                                                                                                                     
---------------------                                                                                                 
 OUTPUT :                                                                                                             
1*2*3*4*17*18*19*20                                                                                                   
--5*6*7*14*15*16                                                                                                      
----8*9*12*13                                                                                                         
------10*11       

*/


#include <stdio.h>

int main()
{
  int i,j,n,count1=0,count2,space=0;
  printf("Enter the number\n");
  scanf("%d",&n);
  printf("---------------------\n OUTPUT :\n");
  count2=n*n+1;
  for(i=n;i>=1;i--)
  {
    for(j=space;j>0;j--)
      printf("-");
    for(j=i;j>=1;j--)
        printf("%d*",++count1);
    for(j=i;j>=1;j--)
    {  
           if(j>1)
           printf("%d*",count2++);
           else
           printf("%d",count2++);
    } 
    
    count2=(count2-1)-2*(i-1);
    space=space+2;
    printf("\n");
  }
  return 0;
}





/*
Enter the number of rows                                                                                               
6                                                                                                                      
     1                                                                                                                 
    1 1                                                                                                                
   1 2 1                                                                                                               
  1 3 3 1                                                                                                              
 1 4 6 4 1                                                                                                             
1 5 10 10 5 1 

*/


#include<stdio.h>
int fact(int num){
    int f=1,i=1;
    while(i<=num)
    {
        f=f*i;
        i++;
    }
    return f;
}
int main()
{
    int i,j,line;
    printf("Enter the number of rows\n");
    scanf("%d",&line);
    
    for(i=0;i<line;i++)
    {
        for(j=0;j<line-i-1;j++)
          printf(" ");
        for(j=0;j<=i;j++)
          printf("%d ",fact(i)/(fact(j)*fact(i-j)));
        printf("\n"); 
    }
    
}


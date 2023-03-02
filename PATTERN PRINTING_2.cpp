

/*
Enter a number                                                                                                         
7   
                                                                                                                   
1                                                                                                                      
22                                                                                                                     
333                                                                                                                    
4444                                                                                                                   
55555                                                                                                                  
666666                                                                                                                 
7777777                                                                                                                
666666                                                                                                                 
55555                                                                                                                  
4444                                                                                                                   
333                                                                                                                    
22                                                                                                                     
1 
    
*/
#include<stdio.h>
int main()
{
    int n,i,j;
    printf("Enter a number\n");
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        for(j=1;j<=i;j++)
         printf("%d",i);
        printf("\n"); 
    }
    for(i=n-1;i>=1;i--)
    {
        for(j=1;j<=i;j++)
         printf("%d",i);
        printf("\n"); 
    }
    return 0;
}


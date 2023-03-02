//PRIME NUMBERS
/*
For an integer to be prime it must be greater than 1, 
and the only integers that divide into it exactly are 1 
and itself such as 3 and 13, etc. 0 is less than 1 so can't be prime. 
Composite integers are those that are the products of primes 
such as 6 = 2x3. 0 cannot be expressed as a product of primes 
because such products are non-zero
Enter a number                                                                                                        
23                                                                                                                    
23 is a prime number


Enter a number                                                                                                        
23                                                                                                                    
23 is a prime number

Enter a number                                                                                                        
1                                                                                                                     
1 is neither prime nor composite

*/

#include<stdio.h>
#include<stdlib.h>
int main()
{
    int num,flag=1,i;
    printf("Enter a number\n");
    scanf("%d",&num);
    if(num==1)
     {
         printf("%d is neither prime nor composite",num);
         exit(0);
     }     
    for(i=2;i<num/2;i++)
    {
        if(num%i==0)
         {
             flag=0;
             break;
         }
    }
    if(flag==1)
     printf("%d is a prime number\n",num);
    else
     printf("%d is not a prime number\n",num);
     
    return 0; 
}


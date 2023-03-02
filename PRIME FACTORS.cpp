//PRIME FACTORS
/*

Enter a number                                                                                                       
36                                                                                                                   
Prime factors are :2 2 3 3  

*/
#include <stdio.h>
int main()
{
  int i,n;
  printf("Enter a number\n");
  scanf("%d",&n);
  printf("Prime factors are :");
  for(i=2;n>1;i++)
  {
      while(n%i==0)
      {
          printf("%d ",i);
          n=n/i;
      }
  }
  return 0;
}


/*
Enter the number of elements                                                                                           
6                                                                                                                      

Enter the elements in the array:
30 20 10 40 50 60                                                                       

The Sorted Array is :                                                                                                  
10 20 30 60 50 40    

*/


#include <stdio.h>
int main()
{
  int i,a[50],n,j,k;
  printf("Enter the number of elements\n");
  scanf("%d",&n);
  printf("Enter the elements in the array:\n");
  for(i=1;i<=n;i++)
    scanf("%d",&a[i]);
  k=n/2;
  
  for(i=1;i<=k;i++)
  {
      for(j=i+1;j<=k;j++)
       {
           if(a[i]>a[j])
           {
               int temp;
               temp=a[i];
               a[i]=a[j];
               a[j]=temp;
           }
       }
  }
  
  for(i=k+1;i<=n;i++)
  {
      for(j=i+1;j<=n;j++)
       {
           if(a[i]<a[j])
           {
               int temp;
               temp=a[i];
               a[i]=a[j];
               a[j]=temp;
           }
       }
  }
  printf("The Sorted Array is :\n");
  for(i=1;i<=n;i++)
  {
      printf("%d ",a[i]);
  }
  
  return 0;
}


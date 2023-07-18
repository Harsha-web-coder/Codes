/*Enter the number of lines for pyramid of stars                                                                         
10                                                                                                                     
         **                                                                                                            
        ****                                                                                                           
       ******                                                                                                          
      ********                                                                                                         
     **********                                                                                                        
    ************                                                                                                       
   **************                                                                                                      
  ****************                                                                                                     
 ******************                                                                                                    
********************

*/



#include <stdio.h>

int main()
{
  int i,j,line;
  printf("Enter the number of lines for pyramid of stars\n");
  scanf("%d",&line);
  
  for(i=1;i<=line;i++)
  {
      for(j=1;j<=line-i;j++)
       printf(" ");
      for(j=1;j<=2*i;j++) 
       printf("*");
    printf("\n");   
  }
  return 0;
}


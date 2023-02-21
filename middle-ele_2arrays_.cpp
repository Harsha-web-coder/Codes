#include<iostream>
using namespace std;
int main()
{
    int arrOne[50], arrTwo[50], arrMerge[100];
	int sizeOne, sizeTwo, i, k;
    cout<<"Enter the Size for First Array: ";
    cin>>sizeOne;
    cout<<"Enter "<<sizeOne<<" Elements for First Array: ";
    for(i=0; i<sizeOne; i++)
    {
        cin>>arrOne[i];
        arrMerge[i] = arrOne[i];
    }
    k = i;
    cout<<"\nEnter the Size for Second Array: ";
    cin>>sizeTwo;
    cout<<"Enter "<<sizeTwo<<" Elements for Second Array: ";
    for(i=0; i<sizeTwo; i++)
    {
        cin>>arrTwo[i];
        arrMerge[k] = arrTwo[i];
        k++;
    }
    int z=sizeOne+sizeTwo;
    int temp,j;
    
	for(i = 0; i<z; i++) {
   for(j = i+1; j<z; j++)
   {
      if(arrMerge[j] < arrMerge[i]) {
         temp = arrMerge[i];
         arrMerge[i] = arrMerge[j];
         arrMerge[j] = temp;
      }
   }}
    cout<<"\nThe New Array :\n";
    for(i=0; i<k; i++)
        cout<<arrMerge[i]<<" ";
        cout<<"\nmiddle element:";
        cout<<arrMerge[i/2];
    
    
    cout<<endl;
    return 0;
}

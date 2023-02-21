#include <bits/stdc++.h>
using namespace std;
int j;
void printDistinct(int arr[], int n)
{
	for (int i=0; i<n; i++)
	{
		for (j=0; j<i; j++)
		if (arr[i] == arr[j])
			break;
		if (i == j)
		cout << arr[i] << " ";
	}
}
int main()
{
	int size,i;
	cout << "Enter the size of an array: ";
	cin >> size;
	int arr[size];	
	for (i = 0; i < size; i++){  
    	cin >> arr[i];
	}
	int n = sizeof(arr)/sizeof(arr[0]);
	cout<<"output:";
	printDistinct(arr, n);
	return 0;
}


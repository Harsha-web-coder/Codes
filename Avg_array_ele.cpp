#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n;
	cout<<"enter num of ele in array";
	cin>>n;
	int a[n];
	for(int i=0;i<n;i++){
		cin>>a[i];
	}
	cout<<"elements in array:";
	for(int i=0;i<n;i++){
		cout<<a[i];
	}
	float sum = 0;
	for (int i=0;i<n;i++){
		sum=sum+a[i];
		}
	cout<<"\naverage is:"<<sum/n;
		
	int x,y;
	float z,q=0;
	z=(a[0]+a[1]+a[n-1]+a[n-2])/4;	
	for(int i=0;i>2;i++){
		q=q+a[i];
		cout<<"\n"<<q;	
	}
	
	
	if(n%2==0){
		if (z==(sum/2) && q==(sum/2)){
			cout<<"True";
		}				
	}
	else{
		cout<<"False";
	}
}




#include<bits/stdc++.h>
using namespace std;
int main(){
	int n;
	cout<<"Enter num of ele in array:";
	cin>>n;
	int a[n];
	for(int i=0;i<n;i++){
		cout<<"Enter Element"<<i+1<<":";
		cin>>a[i];
	}
	cout<<"elements in array:";
	for(int i=0;i<n;i++){
		if(i==n-1){
			cout<<a[i];
			
		}
		else{
			cout<<a[i]<<",";
		}
		
			
	
	}
}

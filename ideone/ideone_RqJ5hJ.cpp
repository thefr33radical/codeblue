#include <iostream>
#include<bits/stdc++.h>
using namespace std;

void count_sort(int arr[],int exp,int size)
{	int count[10]={0};
	int output[size];
	
	for(int i=0;i<size;i++)
			count[(arr[i]/exp)%10]++;
			
	for(int i=1;i<10;i++)
		count[i]+=count[i-1];
		
	for(int i=size-1;i>=0;i--)
		{	output[count[(arr[i]/exp)%10]-1]=arr[i];
			count[(arr[i]/exp)%10]--;
		}
	
	for(int i=0;i<size;i++)	
		arr[i]=output[i];
}


void radix_sort(int arr[],int size)
{	int max=*max_element(arr,arr+size-1);
	for(int i=1; (max/i)>0;i=i*10)
		count_sort(arr,i,size);
	
}


int main() {
	
	int arr[]={10,2,45,3,56,7,6,7,34,98,12};
	int size=(sizeof(arr)/sizeof(arr[0]));
	
	
	radix_sort(arr,size);
	
	for(auto i:arr)
		cout<<i<<" ";
		
	
	return 0;
}
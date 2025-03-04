#include <iostream>
#include<vector>
using namespace std;

void sort(int data[],int low,int mid,int high)
{
	int start1=low,start2=mid+1;
	int k=0;
	int temp[high];
	while(start1<=mid&&start2<=high)
	{	if(data[start1]<=data[start2])	
		temp[k++]=data[start1++];
		else
		temp[k++]=data[start2++];
	}
	
	while(start1<=mid)
		temp[k++]=data[start1++];
	while(start2<=high)
		temp[k++]=data[start2++];
		
		k--;
		for(int i=high;i>=low;i--)
		{	data[i]=temp[k--];
			
		}
	
	
	
}


void merge(int data[],int low,int high)
{	if(low<high)
	{	int mid=(low+high)/2;
		merge(data,low,mid);
		merge(data,mid+1,high);
		sort(data,low,mid,high);
	}
	
}

int main() {
	// your code goes here
	int data[]={12,4,5,65,89,21, 14, 35, 67,8, 28,29};
	
	int size=sizeof(data)/sizeof(data[0]);
	
	merge(data,0,size-1);
	
	
	for(auto i:data)
		cout<<i<<" ";
	return 0;
}
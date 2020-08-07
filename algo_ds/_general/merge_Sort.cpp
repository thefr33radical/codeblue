#include <iostream>
#include<bits/stdc++.h>
#include<vector>
using namespace std;

void sorter(vector<int>&arr,int low,int mid,int high){
	int start1=low,start2=mid+1;
	vector<int>temp;
		for(auto i:arr)
		cout<<i<<" ";
		cout<<endl;
	while(start1<=mid && start2 <=high)
	{	if(arr[start1]<arr[start2])
		{	temp.push_back(arr[start1]);
			start1+=1;
		}
		else
			{	temp.push_back(arr[start2]);
			start2+=1;
		}
	}

	while(start1<=mid)
	{	temp.push_back(arr[start1]);
		start1+=1;
	}
	while(start2 <=high)
	{	temp.push_back(arr[start2]);
		start2+=1;
	}
	int k=0;
	for(auto i=low;i<=high;i++)
		arr[i]=temp[k++];

	// Mistake when copying back copy arr[low]~arr[high]=temp[0]~temp[size]

	for(auto i:arr)
		cout<<i<<" ";

	cout<<" low: "<<low<<" mid "<<mid<<" high "<<high<<endl ;

}


void merge(vector<int>& arr,int low,int high)
{	if(low<high)
	{	int mid=(low+(high-1))/2;
		merge(arr,low,mid);
		merge(arr,mid+1,high);
		sorter(arr,low,mid,high);

	}
}


int main() {
	// your code goes here
	vector<int>arr={1,4,3,6,6,3,8,23,4};

	merge(arr,0,arr.size());
	for(auto i:arr)
		cout<<i;



	return 0;
}

#include <iostream>
#include<bits/stdc++.h>
using namespace std;

void sorter(vector<int>&arr,int low,int mid,int high)
{
	int start1 = low;
	int start2 = mid+1;
	vector<int> temp;
	
	while(start1 <= mid && start2 <= high)
	{
		if(arr[start1]<arr[start2])
			temp.push_back(arr[start1++]);
		if(arr[start2]<arr[start1])
			temp.push_back(arr[start2++]);
	}
	
	while(start1 <= mid)
			temp.push_back(arr[start1++]);
	while(start2 <= high)
			temp.push_back(arr[start2++]);
			
	int k=0;
	
	for(int i=low; i<=high;i++)
	{
		arr[i]=temp[k++];
	}
	
}

void merge_sort(vector<int>&arr,int low,int high)
{
	if(low<high)
	{
		int mid = (low+high)/2;
		merge_sort(arr,low,mid);
		merge_sort(arr,mid+1,high);
	
		sorter(arr,low,mid,high);
	}
	
	
}

int main() {
	// your code goes here
	vector<int> arr({21,34,5,67,3,2,89});
	merge_sort(arr,0,arr.size()-1);
	
	for(auto i :arr)
		cout<<i<<" ";
	
	return 0;
}

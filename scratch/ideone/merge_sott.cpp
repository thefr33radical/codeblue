#include<bits/stdc++.h>
#include <iostream>
using namespace std;

void sort_func(vector<int>& arr,int low,int mid,int high)
{
	int start1= low;
	int start2=mid+1;
	vector<int>temp;
	
	while(start1 <= mid && start2 <= high)
	{
		if (arr[start1] < arr[start2])
		{
			temp.push_back(arr[start1++]);
		}
		else
		{
				temp.push_back(arr[start2++]);
		}
	}
	
	while(start1 <= mid )
		temp.push_back(arr[start1++]);
	while( start2 <= high)
		temp.push_back(arr[start2++]);
		
	int k=0;
	for(int i=low;i<=high;i++)
	{
		arr[i]=temp[k++];
	}
	
}



void merge_sort(vector<int>&arr, int low,int high)
{	
	if (low<high)
	{
		int mid = (low+high)/2;
		merge_sort(arr,low,mid);
		merge_sort(arr,mid+1,high);
		sort_func(arr,low,mid,high);
	}
}


int main() {
	// your code goes here
	
	vector<int> arr({12,1,326,65,88,54,97,24});
	//cout<<arr.size();
	merge_sort(arr,0,arr.size()-1);
	
	for(auto i:arr)
		cout<<i<<" ";
	return 0;
} 

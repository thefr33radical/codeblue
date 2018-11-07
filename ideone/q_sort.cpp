#include <iostream>
#include<bits/stdc++.h>

using namespace std;

int sorter(vector<int> & arr, int low,int high)
{
	int pivot =low;
	int pe=arr[pivot];
	
	int i= low+1;
	int j=high;
	int temp;
	
	while(i<j)
	{
		while(arr[i]<pe)
		{
			i++;
		}
		
		while(arr[j]>pe)
		{
			j--;
		}
		if(i<j)
		{
		temp=arr[i];
		arr[i]=arr[j];
		arr[j]=temp;
		i++;
		j--;
		}
	}
	
	
	arr[low]=arr[j];
	arr[j]=pe;
	
	return j;
}

void q_sort(vector <int>&arr,int low,int high)
{
	if(low<high)
	{
		int pivot=sorter(arr,low,high);
		cout<<"\npivot"<<pivot<<" "<<arr[pivot];
	
		q_sort(arr,low,pivot-1);
		q_sort(arr,pivot+1,high);
		
	}
		for(auto i:arr)
			cout<<" ";
	
}

int main() {
	// your code goes here
	
	vector<int> arr({12,45,2,34,21,87,9,6});
	
	q_sort(arr,0,arr.size()-1);
	cout<<"\n";
	for(auto i:arr)
		cout<<i<<" ";

	return 0;
	
	
}

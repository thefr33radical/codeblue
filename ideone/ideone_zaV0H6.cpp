#include<iostream>
#include<bits/stdc++.h>

using namespace std;


void sort(vector<int> &data, int low, int mid,int high)
{	int start1=low,start2=mid+1;
	vector<int>temp;
	
	while(start1<=mid && start2 <= high)
	{	if(data[start1]<=data[start2])
			temp.push_back(data[start1++]);
			
		else
			temp.push_back(data[start2++]);
	}
	
	while(start1<=mid)
		temp.push_back(data[start1++]);
	
	while(start2<=high)
		temp.push_back(data[start2++]);
		
	int k=temp.size()-1;
	for(auto i=high;i>=low;i--)
		data[i]=temp[k--];
}




void merge(vector<int> &data,int low,int high)
{	if(low<high)
	{	int mid=floor((low+high)/2);
		merge(data,low,mid);
		merge(data,mid+1,high);
		sort(data,low,mid,high);
	}
}	

int main()
{
	vector<int> data={12,4,5,65,89,21, 14, 35, 67,8, 28,29};
	merge(data,0,data.size()-1);
	
	for(auto i:data)
		cout<<i<<"\t";
	
return 0;	
}

#include<bits/stdc++.h>

using namespace std;

int sort(vector<int>&arr,int low,int mid,int high)
{	int start1=low;
	int start2=mid+1;
	vector<int>temp;
	while(start1<mid&&start2<=high)
	{	if(arr[start1]<arr[start2])
			temp.push_back(arr[start1++]);
		else
			temp.push_back(arr[start2++]);
	}
	while(start1<mid)
		temp.push_back(arr[start1++]);
	while(start2<=high)
		temp.push_back(arr[start2++]);
	
	int k=temp.size()-1;
	for(int i=0;i<temp.size();i++)
		arr[i]=temp[k--];

return 1;
}


int merge(vector<int>&arr,int low,int high)
{	if(low<high)
	{	mid=low+high/2;
		merge(arr,low,mid);
		merge(arr,mid+1,high);
		sort(arr,low,mid,high);
return 1;
}



int main()
{	
	vector<int>arr={56,3,46,53};
	merge(arr,0,arr.size()-1);
	for(i:arr)
		cout<<i<<" ";	
return 0;
}

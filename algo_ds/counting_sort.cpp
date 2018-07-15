#include<bits/stdc++.h>
using namespace std;
int main()
{

    vector<int>arr{1,2,3,9,6,33,2};
    vector<int>op(arr.size(),0);
    int max_e=*max_element(arr.begin(),arr.end());
    vector<int>count(max_e,0);

    for(int i=0;i<arr.size();i++)
    {
        count[arr[i]]++;
    }

for(int i:count)
        cout<<i<<" ";
     cout<<"\n";
    for(int i=1;i<count.size();i++)
    {
        count[i]=count[i-1]+count[i];
    }
    for(auto i:count)
        cout<<i<<" ";
     cout<<"\n";

     for(int i=0;i<arr.size();i++)
    {
        op[count[arr[i]]-1]=arr[i];
        count[arr[i]]--;
       }

    for(int i:op)
        cout<<i<<" ";
    
    
    cout<<"\n";
    for(int i:count)
        cout<<i<<" ";

    return 0;
}

/*
#include <iostream>
#include<bits/stdc++.h>
using namespace std;



void sort(vector<int>&arr)
{
	int maximum=*max_element(arr.begin(),arr.end());
	vector<int>count(10,0);
	vector<int>output(arr.size(),0);
	
	for(auto i=0;i<arr.size();i++)
	{
		count[arr[i]]++;
	}
	// Count array gives the position of the element
	for(auto i=0;i<count.size();i++){
		count[i]+=count[i-1];
	}
	
	for(auto i=0;i<arr.size();i++)
	{
		output[arr[count[i]]]=arr[i];
		count[i]--; 	
	}
	
for(auto i=0;i<arr.size();i++)
{
	arr[i]=output[i];
}
	
}

int main() {
	// your code goes here
	vector<int> arr{2,45,32,54,21,56,6};
	sort(arr);
	for(auto i:arr)
	cout<<" "<<i;
	return 0;
}*/

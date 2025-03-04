#include<bits/stdc++.h>
using namespace std;

int max_value(vector<int>& arr)
{
    int maximum=max_element(arr,arr.begin(),arr.end());
    
    return maximum;
}

void radix(vector<int>&arr, int exp)
{
	
	
}


void sorter(vector<int>&arr)
{
    int max_value=max_value(arr);
    for(int i =1;i<max_value;i=i*10)
   {	radix(arr,i);
   	
   }

	
	
}



int main()
{
    vector<int> arr({10,21,3,300,43,354,99,84,101});
   
   sorter(arr);


    return 0;
}
/*
Sorting array with reverse around middle

make a copy of array
Sort array2
compare sorted array[i] with arr2[length -i]
T(C)= O(nlogn) + 2 X O(n)

*/

#include <iostream>
#include<bits/stdc++.h>

using namespace std;

int main() {
	// your code goes here
	vector<int>arr;
	
	int temp;
	
	while(cin>>temp)
		arr.push_back(temp);
	
	vector<int>arr2;
	arr2=arr;
	
	sort(arr.begin(),arr.end()); //n log n
	int l=arr.size()-2;
	for(auto i=1; i<arr.size()-1;i++)
 		{   if(arr[i]==arr2[l])	
 			{	
 				cout<<arr[i]<<" "<<arr2[l];
 				l--;
 				cout<<"\n";
 				continue;
 			
 			}
 		    if(arr[i]==arr2[i])	
 			{	cout<<arr[i]<<" "<<arr2[i];
 				l--;
 				cout<<"\n";
 				continue;
 			
 			}
 		    else
 			{
 		    	cout<<"Not possible";
 		    	cout<<arr[i]<<" "<<arr2[l];
 		    	return 0;
 			}
		}
	cout<<"Possible";
	
	return 0;
} 

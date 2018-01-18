// Row Major Ordering and Column Major Ordering

#include <iostream>
#include<bits/stdc++.h>

using namespace std;

int main() {
	int n,temp;
	vector<int> arr;
		
	
	cout<<" Enter 1 for row major ordering, 2 for column major ordering";
	cin>>n;
	
	cout<<"\n Enter the array";
//cin>>temp;
	while(cin>>temp)
	{	arr.push_back(temp);
	
	}
	cout<<"\n\n";

	int i=0;
	while(arr[i])
	{	int j=0;
		while(j<n)
		{	if(arr[i])
				cout<<arr[i];
			else
				break;
			i++;
			j++;
		}
		cout<<"\n";
	
	}
	return 0;
	}
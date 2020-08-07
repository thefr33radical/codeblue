/*
majority-element
T(C)= O(n) + O(n)

*/

#include<bits/stdc++.h>
#include <iostream>
using namespace std;

int main() {

	map<int,int> m;
	vector<int> arr{2,2,2,2,5,5,2,3,3};
	int temp,size;
	auto i =arr.begin();

	while(i!=arr.end())
	{		temp=*i;

			m[temp]++;
			size++;
			i++;
	}

	for(auto i:m)
		{
				if(i.second > size/2)
				cout<<"majority found "<<i.first<<" "<<i.second<< "\n";
				return 0;
		}

	cout<<"majority not found";
	// your code goes here
	return 0;
}

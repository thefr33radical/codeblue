#include <iostream>
#include<bits/stdc++.h>
using namespace std;



int main() {
	int temp;
	map<int,int> counter;
//	vector<int> inp;
	while(cin>>temp)
	{
		counter[temp]++;
		
	}
	
	for(auto i:counter)
	{	if((i.second)>1)
			cout<<(i.first)<<" "<<(i.second)<<endl;	
	}
	
	
	// your code goes here
	return 0;
}
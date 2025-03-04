#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int m=5;
	int n=6;
	vector<vector<int>>matrix(m,vector<int>(n,0));
	
/*
0 0 0 0 0 
0 0 0 0 
0 0 0 
0 0 
0 

	for(auto i=0;i<m;i++)
	{
	 
		for(auto j=0;j<n;j++)
		{
			if(i<j)
			{
				cout<<matrix[i][j]<<" ";
			}
		}
		cout<<"\n";
	}
	

		for(auto i=0;i<m;i++)
	{
	 
		for(auto j=0;j<n;j++)
		{
			if(i>j)
			{
				cout<<matrix[i][j]<<" ";
			}
		}
		cout<<"\n";
	}
	

	
		for(auto i=0;i<m;i++)
	{
	 
		for(auto j=0;j<n;j++)
		{
			if(i>j)
			{
				cout<<matrix[i][j]<<" ";
			}
		}
		cout<<"\n";
	}
	
*/	
	
	
	for(auto i=0;i<m;i++)
	{
	{ for(auto j=i;j<n;j++)
		
	
	cout<<i<<j<<" ";
	}
	cout<<"\n";
	}
	

	
	return 0;
}
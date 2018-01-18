#include <iostream>
#include<bits/stdc++.h>
using namespace std;

long noofmonk(vector<long >&index,long val1,long val2)
{	
	long c=0;
	for(int i=val1;i<val2-1;i++)	
	c++;
	
	cout<<"\nmonkey retur:"<<c;
	return c;
	
	
}

int main() {
	// your code goes here
	int t;
	string inp;
	
	cin>>t;
	vector<string> v;
	while(t)
	{
		cin>>inp;
		v.push_back(inp);
	
		t--;
	}
	
	
	vector<long>index,number;
	long median;
	long arr;
	int cont=-1,right=0,supercont=0;
	for(auto x:v)
	{//	arr=i;
	long count=0;
	long median;
	long val=0;
		for(auto j:x)
			{ 
				number.push_back(j-'0');
				if(j-'0'==1)
					index.push_back(count);
				count++;
			}
		//	cout<<"\nindex"<<index.size();
		
				 median=(index.size()+1)/2;
		
		cout<<"\n median"<<index[median];
			int i=number[median];
			int start=i;
			while(i<number.size())
			{	cont++;
				if(number[i]==1)
				{		right++;
						start++;
				
					number[i]=0;
					supercont=cont;
					i=start;
					cont=-1;
				}
				
			i++;	
			}
			val=supercont-right;
		cout<<"\n"<<val;	
		cout<<endl;
		
	}
	return 0;
}
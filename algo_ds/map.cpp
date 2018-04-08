#include <iostream>
#include<bits/stdc++.h>
#include<map>
using namespace std;

int main()
{
	int n;
map<int,int>::iterator it;
map<int,int> mapper;

while(1)
{
cin>>n;// input number
if(n==0)
	break;

if(mapper[n]==1)
	cout<<"duplicate";
else
	mapper[n]=1;

}

for(it=mapper.begin();it!=mapper.end();it++)
	cout<<it->first<<":::"<<it->second;


//cout<<mapper.max_size();

	return 0;
}

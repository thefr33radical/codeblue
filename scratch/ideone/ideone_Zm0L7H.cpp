#include <iostream>
#include<bits/stdc++.h>

using namespace std;

int main() {
	// All possible substring

string str,temp;
vector<string> s;
cin>>str;

for(int i=1;i<=str.length();i++)
{
	for(int j=0;j<=str.length()-i;j++)
		{	
			int x=i+j-1;
			for(int k=j;k<=x;k++)
					cout<<str[k];
			cout<<endl;
		}

}

//\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\method 2
cout<<endl;
	for(int i=0;i<=str.length();i++)
{cout<<endl;
	for(int j=0;j<=str.length()-i;j++)
		cout<<str.substr(i,j)<<"\t";
}




	return 0;
}
#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	vector<string> repl;
	vector<string> str2;
	string temp;
	string temp2;
	getline(cin,temp);
	int i=0;
	
	while(i<temp.length())
	{	temp2=temp[i];
		repl.push_back(temp2);
	
		cout<<temp[i];
			i++;
	}
	
	getline(cin,temp);
	i=0;
	cout<<"\n";
	
	while(i<temp.length())
	{	temp2=temp[i];
		str2.push_back(temp2);
		cout<<temp[i];
		i++;
	}
	
	for(i=0;i<str2.length();i++)
		{	int j=0;
				
				for(j=0;j<i.length();i++)
				{
					if(i[j]=='{')
						{
							if(i[j+1]=='}')
							if(isnum(i[j+1]))
							{
								cout<<repl[tonum]
							}
						}
					
				}
		}
	
	return 0;
}
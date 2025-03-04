//
 
#include <iostream>
#include<bits/stdc++.h>
using namespace std;
 
void lcsubstr()
{
	string str1="OldSite:GeeksforGeeks.org";
 	 string  str2="NewSite:GeeksQuiz.com";

	int len2=str2.size()+1;
int len1=str1.size()+1;
	vector< vector<int> > res(len2);
	
	for(int i=0;i<len2;i++)
	{	res[i].resize(len1,0);
	}
int max=0;
 	for(int i=1;i<str2.size();i++)
	{
		for(int j=1;j<str1.size();j++)
		{
		if (str1[i-1] == str2[j-1])
           {  res[i][j] = res[i-1][j-1] + 1;
				if(res[i][j]>max)
					max= res[i][j];
		}
	cout<<res[i][j];
	}
	cout<<"\n";
}


cout<<"\n\n Max length:"<<max;
}
int main()
{

lcsubstr();

return 0;
}
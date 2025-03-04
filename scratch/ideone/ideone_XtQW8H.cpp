#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int check(string str,int index)
{	long j=str.length()-1;
   	for(int it=0;it <str.length()&&j >-1;it++)
        {  
        if(str[it]!=str[j])
            {              return 0;
            }
        j--;
    }
    cout<<index<<"\n";
    return 1;
}


void func(string str)
{   string temp=str;
	//cout<<temp;
	if(check(temp,-1))
	   return;
 
 	string x;
	for(int it=0;it <temp.length();it++)
	{
   for(int j=0;j<temp.length()-it;j++)
   	{	x=temp.substr(it,j);
   		if(x.length()==temp.length()-1)
   			if(check(x,it))
	   			return;
		}
	}
}


int main() {
    string str,temp;
    vector<string>s;
    int inp;
    cin>>inp;
    while(inp--)
        {   cin>>str;
          s.push_back(str);
        }
    for(int it=0;it <s.size();it++)
	 func(s[it]);
    
  
    return 0;
}

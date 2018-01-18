#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<math>

#include<stack>
using namespace std;


int main()
{   
    string str;
    
    cin>>str;

    stack<string> stck;
	
 for(int it=0;it<str.length();it++)
	{	if(stck.empty())
			{	stck.push(str[i]);
			continue;
			}
		if(stack.top()==str[i])
			{	stck.pop();
				i=i+1;
			}

		
   
     for(int it=0;it<str.length();it++)
             cout<<str[it];
   
    return 0;
}

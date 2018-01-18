#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<stack>
using namespace std;


int main()
{   string str;
    cin>>str;
  /*  
    for(int it=0;it<str.length();it++)
        {
        
        if((str[it])==(str[it+1]))
      {
          //  str.insert(it,"0");
          //  str.insert(it+1,"0");
            str.erase(it,2);
          it=0;
         //cout<<"del";
          
        }
       
    }
    
    */
        stack<char> stck;
	
 for(int it=0;it<str.length();it++)
	{	if(stck.empty())
			{	stck.push(str[it]);
		//	cout<<stck.top();
			continue;
			}
		if(stck.top()==str[it])
			{	//cout<<stck.top();
            stck.pop();
          //  it=it-1;
				//it=it+1;
			}
			else
				stck.push(str[it]);

    }
    vector<char> a;
 
    if(stck.empty())
        {
        cout<<"Empty String";
        return 0;
    }
     while(!stck.empty())
           {  a.push_back(stck.top());
                stck.pop();
           }
   
    for(auto it=a.rbegin();it!=a.rend();it++)
        cout<<*it;
 
 return 0;
}


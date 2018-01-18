#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<bits/stdc++.h>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    
    string str,rstr;
    vector<string> sets;
    int n;
    cin>>n;
   
    
    while(n--)
        {   
         cin>>str;
        sets.push_back(str);
      }
    
    int flag=0;
    
    
    for(auto it=sets.begin();it!=sets.end();it++)
    {
    string temp=*it;
    cout<<temp.length();
        for(int i=1,j=temp.length()-1;i<temp.length()-1&&j>=0;i++,j--)
                 {
                  int x=temp[i]-temp[i-1];
                  int y=temp[j]-temp[j-1];
                 cout<<"temp[i-1]"<<temp[i];
                        if(temp[i]-temp[i-1]!=temp[j]-temp[j-1])
                            {
                            flag=1;
                            
                            }
          }
    }
    
    if(flag==1)
    cout<<"\n not funny";
    
    return 0;
}


/*
Given an expression exp of length n consisting of some brackets. 
The task is to print the bracket numbers when the expression is being parsed.

Eg :
(a+(b*c))+(d/e)
1 2 2 1 3 3
*/


#include<bits/stdc++.h>
using namespace std;



int main()
{
    String s;
    cin>>s;
    stack<pair<char,int>> stk;
    int counter=0;
    for(int i=0; i<s.length(); i++)
    {
        if(s[i]=="(")
        {
            stk.push(make_pair("(",++count));
        }

         if(s[i]==")")
        {
            stk.push(make_pair("(",--count));
        }


    }

    for(auto i:stk)
        cout<<i;

    return 0;
}

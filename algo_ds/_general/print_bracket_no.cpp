
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
    char s[15];
    cin>>s;
	
    stack<pair<char,int> > stk;
    stack<int>count;
    int counter=0;
     for ( int i=0; i<15;i++)
    {
	if(s[i]=='(')
        {	++counter;
            count.push(counter);
            stk.push(make_pair('(',count.top()));
            //counter++;
        }
         else if(s[i]==')')
        {
            stk.push(make_pair(')',count.top()));
            count.pop();
           // counter--;
        }


    }

    for(; !stk.empty();)
    {
	cout<<stk.top().second<<" ";
	stk.pop();
    }

    return 0;
}
    
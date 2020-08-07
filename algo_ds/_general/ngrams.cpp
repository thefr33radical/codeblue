#include<bits/stdc++.h>
using namespace std;

string gen(string text[],int i,int n)
{
    string temp="";
    for(int j=i;j<i+n;j++)
    {    temp=temp+text[j];
        //    cout<<temp<<"\n";
               }
    return temp;
}


void grams(string text[],int n)
{    n=n-1;
    for(int i=0;i<6-n;i++)
        {   temp[i]=(text[i]+gen(text,i+1,n));
            cout<<temp[i]<<"\n";
        }
}


int main()
{   string text[]={ "i ","am ","here","how","are","you"};

    int ngram;
    grams(text,2);

return 0;
}





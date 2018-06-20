#include<bits/stdc++.h>
using namespace std;
int main()
{

    vector<int>arr{1,2,3,51,6,34,23};
    vector<int>op(arr.size(),0);
    double max_e=*max_element(arr.begin(),arr.end());
    vector<int>count(max_e,0);

    for(int i=0;i<arr.size();i++)
    {
        count[arr[i]]++;
    }


    for(int i=1;i<count.size();i++)
    {
        count[i]=count[i-1]+count[i];
    }

     for(int i=0;i<arr.size();i++)
    {
        op[count[arr[i]]-1]=arr[i];
        count[arr[i]]--;
       }

    for(int i:op)
        cout<<i<<" ";

    return 0;
}
#include<bits/stdc++.h>
using namespace std;
int main()
{

    int a[]={6,5,1,7,2,4,3};
    stack<int> s;
    vector<int> arr(a,a+7);

    s.push(arr[0]);
    for(int i=1;i<arr.size();i++)
    {

       while( s.top()< arr[i] && (!s.empty()))
        {
            cout<<s.top()<<" next greater element -->"<<arr[i]<<"\n";
            s.pop();
        }
        s.push(arr[i]);


    }

    if(!s.empty())
        cout<<"fvfg";



    return 0;
}

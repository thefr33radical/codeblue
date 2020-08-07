#include<bits/stdc++.h>

using namespace  std;

int main()

{
map<int,int> mapper;
map<int,int>::iterator it;

int n,x;


cin>>x;
while(1)
    {
    cin>>n;

    if(n==0)
        break;


    if(mapper[x-n]==(x-n))
    {
        cout<<mapper[x-n];
        cout<<"sum exits";

        }
    else

        mapper.at(n)=n;
}
for(it=mapper.begin();it!=mapper.end();it++)
{
cout<<it->first<<"***"<<it->second;
cout<<"\n";
}

return 0;

}

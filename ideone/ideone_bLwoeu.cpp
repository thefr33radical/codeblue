
#include<bits/stdc++.h>

using namespace std;
void stairs(int n,int m)
{
    int res[n];

res[0]=1;
res[1]=1;
for(int i=2;i<n;i++)
    {res[i]=0;
        for(int j=1;j<=m&&j<=i;j++)
            res[i]=res[i-j]+res[i];
// cout<<res[i-1]<<"\t";
    }

    cout<<res[n-1];
}
int main()
{	
	int n,m;
    cout<<"Enter number of stairs:";
    cin>>n;

    cout<<"\nEnter number of stairs u can skip";
    cin>>m;

    stairs(n+1,m);

    return 0;
}

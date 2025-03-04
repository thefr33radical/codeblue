// four arrow keys

#include <iostream>
#include<bits/stdc++.h>
using namespace std;

void arrow()
{
 int N=20;
vector<int> res(20,0);

for(int i=1;i<=6;i++)
{	res[i-1]=i;
	}
for(int i=7;i<=N;i++)
	{	res[i-1]=0;
		for(int j=i-3;j>=1;j--)
			{	int curr=res[j-1]*(i-j-1);
				if(curr>res[i-1])
					res[i-1]=curr;
			}
	}
cout<<res[N-1];

}



int main() {
	arrow();
	return 0;
}
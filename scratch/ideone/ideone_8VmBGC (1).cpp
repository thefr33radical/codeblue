#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main()
{
	
	int n,count[20],i,j;
	char a[200];
	
	gets(a);
	
	for(i=0;i<n;i++)
	{
		count[i]=1;
	}
	
	i=0;
	j=0;
	
	while(i<n&&j<n)
	{
		
		if(a[i]==a[i+1])
		{
			i++;
			count[j]++;
			continue;
		}
		
		else
		{
			
			cout<<a[j];
		}
		if(count[j]>1)
		cout<<count[j];
		i++;
		j=i;
		continue;
	}
		
	}
	
    return 0;
}

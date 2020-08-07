


#include<bits/stdc++.h>
#include<iostream.h>

using namespace std;




int main()
{
	int arr[][]= {{1,2,3},{4,5,8},{4,5,8},{11,29,43}};
	
	
int arr[][]=msort(arr[0],arr[1]);
	
	for(int i=2;i<arr.size()-1;i++)
	{
		c=msort(c,arr[i]);
	}
	

for(int i =0;i<4;i++)
{
	for(j=0;j<3;j++)
	{
		cout<<c[i][j];
	}
}
	
	
	
	
	
}

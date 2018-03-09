
#include<bits/stdc++.h>

using namespace std;

int main()
{	queue<int,int> q;
	int mat[3][4]={{1,3,5,8},{4,2,1,7},{4,3,2,3}};
	
	int val[3][4];
	
	val[0][0]=mat[0][0];
	
//Initialize top row and first column with sum of elements for their respective cells
	for(auto i=1;i<3;i++)
		val[i][0]=mat[i][0]+val[i-1][0];
	
	for(auto i=1;i<4;i++)
		val[0][i]=mat[0][i]+val[0][i-1];

//Compute min cost path using DP		
	for(auto i=1;i<3;i++)
	{	for(auto j=1;j<4;j++)
		{	val[i][j]=min(val[i-1][j],val[i][j-1])+mat[i][j];
			
		}
	}
	
// Print the value matrix which contains the total cost path
	
	for(auto i=0;i<3;i++)
	{	for(auto j=0;j<4;j++)
		{	cout<<val[i][j]<<" ";
			
		}
		cout<<"\n";
	}
	
	
for (int i=2;i>0;i--)
{	for(int j=3;j>0;j--)
	{	if(val[i-1][j]<val[i][j-1])
			q.push(make_pair(i-1,j));
	
		else
			q.push(make_pair(i,j-1));
	}
}
	
	for(auto i:q)
	cout<<i;
	
	
}
 #include <iostream>
#include<bits/stdc++.h>
using namespace std;

void subset_sum(vector<int> &arr,int rows,int cols)
{	

for(int i =1; i<rows;i++)
	{		for(int j=1;j<cols;j++)
		{	if(j<array[i-1])
				{
				matrix[i][j]=matrix[i-1][j];
				}	
			else
			{
				matrix[i][j]=matrix[i-1][j]||matrix[i-1][j-array[i-1]];
				
			}
		}
	}
	
	for(auto i:matrix)
	{
		for(auto j:i)
		{
			cout<<j<<" ";
		}
		cout<<"\n";
	}
	
}

int main()
{
	vector<int> array({1,2,3,4,5});
	int total = 6;
	int rows = array.size()+1;
	int cols = total+1;

	vector< vector<int> > matrix(rows,vector<int>(cols));
	
	for(int i =1; i<rows;i++)
		matrix[i][0]=1;

	subset_sum(matrix,rowws,cols);	
	return 0;

}


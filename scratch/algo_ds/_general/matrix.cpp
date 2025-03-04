#include <iostream>
using namespace std;

int main()
{
	// your code goes here

	int n;
cin>>n;
	int mat[n][n];
	int left =0,right=n-1,top=0,bottom=n-1,temp=0;

	while(left<right&&top<bottom)
	{
		for(int i=left;i<=right;i++)
		{	temp++;
			mat[top][i]=temp;

		}

    top++;
			for(int i=top;i<=bottom;i++)
		{	temp++;
			mat[i][right]=temp;

		}
right--;
			for(int i=right;i>=left;i--)
		{	temp++;
			mat[bottom][i]=temp;

		}
		 bottom--;
			for(int i=bottom;i>=top;i--)
		{	temp++;
			mat[i][left]=temp;

		}

  left++;

	}

	for(int i=0;i<n;i++)
	{
		for(int j=0;j<n;j++)
		{
			cout<<mat[i][j]<<"\t";

		}
		cout<<"\n";

	}

	return 0;
 }

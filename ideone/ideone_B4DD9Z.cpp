#include <iostream>
using namespace std;

int isSubsetSum(int set[],int n,int number)
{	int mat[n+1][number+1];
	
	for(int i=0;i<=n;i++)
	{	for(int j=0;j<=number;j++)
		{	mat[i][j]=0;
		}
	}
	
	
	for(int i=0;i<=n;i++)
	{	for(int j=0;j<=number;j++)
		{	if(i==0)
				{	mat[0][j]=0;
				}
			else if(j==0)
				{	mat[i][0]=1;
				}
			else if (j>=set[i])
				{
					mat[i][j]=(mat[i-1][j]||mat[i-1][j-set[i]]);
				}
				
			else
					mat[i][j]=mat[i-1][j];
				
				cout<<mat[i][j]<<"\t";
		}
		cout<<"\n";
	}
return mat[n][number];

}


int main() {
	int set[] = {1,2,3,4,5,6,7,8,9,10};
  int sum = 55;
  int n = sizeof(set)/sizeof(set[0]);
  if (isSubsetSum(set, n, sum))
     printf("Found a subset with given sum");
  else
     printf("No subset with given sum");
  return 0;
}
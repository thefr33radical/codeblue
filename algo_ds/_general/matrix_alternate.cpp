#include<bits/stdc++.h>
using namespace std;

int main()
{	 int m=4,n=4;
    vector<vector<int> > mat(m,vector<int> (n));

   int top_left=0,right=n-1,bottom_left=m-1,bottom_right=m-1;
   int mov_right=0,mov_bottom=0,mov_left=n-1,mov_up=m-1;
   int alt=0;
   while(top_left<right || bottom_left >top_left)
   {
	while(mov_right<=right)
	{
		mat[mov_bottom][mov_right++]=alt;
		
	}
	
	mov_right--;
	while(mov_bottom<=bottom_right)
	{
		mat[mov_bottom++][mov_right]=alt;
		
	}
	mov_bottom--;
	while(mov_left>=bottom_left)
	{
		mat[mov_bottom][mov_left--]=alt;
		
	}
   	mov_left++;
   	while(mov_up>=top_left)
	{
		mat[mov_up--][mov_left]=alt;
		
	}
   	
   	top_left++,right--,bottom_left--,bottom_right--;
   	if(alt==0)
   	alt=1;
   	else
   	alt=0;
   	
   	
   }
 for(int i=0;i<m;i++)
    {
        for(int j=0;j<n;j++)
        {
           cout<<mat[i][j]<<"\t";
        }
            cout<<"\n";
    }
    


    return 0;
}
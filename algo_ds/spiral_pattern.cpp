/*

Program to print spiral pattern in a matrix
T(c)=O[(n)X(n)]
*/

#include<bits/stdc++.h>
using namespace std;


void compute()
{
    int m=3,n=4;
    vector<vector<int> > mat(m,vector<int>(n));

   int top_left=0,top_right=n-1,bottom_left=0,bottom_right=m-1;
   int mov_right=0,mov_down=0,mov_left=n-1,mov_up=m-1;
   int count =0;

    while(top_left<top_right && bottom_right>top_left)
    {
        while(mov_right<top_right)
        {   mat[top_left][mov_right]=count++;
            mov_right++;
            
        }
         while(mov_down<bottom_right)
        {   mat[bottom_right][mov_down++]=count++;
           
        }
         while(mov_left>bottom_left)
        {   mat[bottom_left][mov_left--]=count++;
            
        }

          while(mov_up>top_left)
        {   mat[top_left][mov_up--]=count++;
            
        }

        top_left++;
        top_right--;
        bottom_right--;
        bottom_left--;
        mov_right=top_left;
        mov_down=top_right;
        mov_left=bottom_right;
        mov_up=bottom_left;

    }

    for(int i=0;i<mat.size();i++)
    {   for(int j=0;j<mat[0].size();j++)
            cout<<mat[i][j]<<"\t";

        cout<<"\n";


    }


}

int main()
{
    compute();

    return 0;
}
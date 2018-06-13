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

  int bottom=m-1;
  int right=n-1;
  int left=0;
  int top=0;
 

   int mov_right=0,mov_left=right,mov_up=bottom,mov_down=0;
   int count =0;

    while(top<bottom || left<right)
    {
        while(mov_right<right)
        {   mat[top][mov_right]=count++;
            mov_right++;
            
        }
         while(mov_down<bottom)
        {   mat[right][mov_down++]=count++;
           
        }
         while(mov_left>left)
        {   mat[bottom][mov_left--]=count++;
            
        }

          while(mov_up>top)
        {   mat[left][mov_up--]=count++;
            
        }

        top++;
        bottom--;
        left++;
        right--;

        mov_right=left;
        mov_down=top;
        mov_left=right;
        mov_up=bottom;

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
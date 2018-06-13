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

   int top=0, left=0, right=n-1, bottom=m-1;
    int count=1;
    int mov_right=left, mov_down=top, mov_up=bottom, mov_left=right;

    while(top<=bottom && left<= right)
    {
        while(mov_right<right)
        {
            mat[top][mov_right++]=count++;
        }


        while(mov_down<bottom)
        {
            mat[mov_down++][right]=count++;
        }

         while(mov_left>left)
        {
            mat[bottom][mov_left--]=count++;
        }

         while(mov_up> top)
        {
            mat[mov_up--][left]=count++;
        }

        top++,left++, right--, bottom--;
        mov_right=left, mov_down=top, mov_up=bottom, mov_left=right;
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
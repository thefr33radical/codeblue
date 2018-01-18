#include<bits/stdc++.h>

using namespace std;

void convert(int sum)
{
    vector<int> binary;
    int rem;
    int tmp=sum;

    while(tmp)
    {
    rem=tmp%2;
    binary.push_back(rem);
    tmp=tmp/2;
    }

   
    for(vector<int>::reverse_iterator it=binary.rbegin(); it!=binary.rend(); it++)
        cout<<*it;




}
void compute()
{

    unsigned long v,e,v1,v2,power;
    cin>>v>>e;
    
    if(v>100000||v<1)
        return;
    
     if(e>2*100000||e<1)
        return;

    unsigned long temp=e;
    unsigned long mat[v][v];

     for(unsigned long i=0;i<v;i++)
            {   for(unsigned long j=0;j<v;j++)
                {
                mat[i][j]=99999;

               }
               
            }
    while(temp)
    {   cin>>v1;
        cin>>v2;
        cin>>power;

        power=pow(2,power);
        //cout<<power;
        mat[v1-1][v2-1]=power;
        mat[v2-1][v1-1]=power;
        temp--;
     }
     
    unsigned long  i, j, k;
    for (k = 0; k < v; k++)
    {   for (i = 0; i < v; i++)
        {   for (j = 0; j < v; j++)
            {   if (mat[i][k] + mat[k][j] < mat[i][j]&&(i!=j))
                    mat[i][j] = mat[i][k] + mat[k][j];
            }
        }
    }

  
     int sum =0;
     for(unsigned long i=0;i<v;i++)
        {   for(unsigned long j=0;j<v;j++)
            {   if(mat[i][j] == 9999 || i==j)
                break;
            else
                sum =sum+mat[i][j];
            }
              }
    convert(sum);
}
int main()
{
   compute();

    return 0;
}






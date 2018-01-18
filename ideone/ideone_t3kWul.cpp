#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<bits/stdc++.h>
using namespace std;

// keep it simple

class cutting_rod
{
public:
    void compute()
    {
    vector<pair<int,int> >data;
    //vector<int,vector<int> >mat;
    int length,l,profit;
    cout<<"\n Enter total length:";
    cin>>length;
    cout<<"\n Enter  length, profit: enter length 999 to stop";
    while(1)
    {
        cin>>l;
        if(l==999)
            break;
        cin>>profit;
        data.push_back((make_pair(l,profit)));
    }
    vector< vector<int>  >mat;
    mat.resize(data.size()+1);
    for(int i=0;i<data.size()+1;i++)
    {
        if(i==0)
            mat[i].resize(length+1,0);

        mat[i].resize(length+1);
    }
         for(int i=1;i<data.size()+1;i++)
         {  for(int j=1;j<length+1;j++)
                {   if(i==1)
                    {   if(j>=data[i].first)
                            mat[i][j]=mat[i][j-data[i-1].first]+data[i-1].second;// mat[i][j]=mat[i][j-leni] + profit[i-1]

                    		mat[i][j]=data[i-1].second;
                    }

                if(j>=data[i-1].first)
                    {     mat[i][j]=max(mat[i][j-data[i-1].first]+data[i-1].second,mat[i-1][j]);

                 //mat[i][j]=max( mat[i][j-leni] + profit[i-1], mat[i-1][j]) maxof(mat[i][j-leni]+profit[i-1],top cell)
                    }
                else
                    mat[i][j]=mat[i-1][j];
                    cout<<mat[i][j]<<"\t";
                    }
            cout<<"\n";
        }
    vector<int> sequence;
    int i=data.size();
    int j=length;
    
    			while(i>=1&&j>=1)
                {   if(mat[i][j]==mat[i-1][j])
                    {   sequence.push_back(mat[i][j]);
                        i=i-1;
                    }
                    else{
                       
                        sequence.push_back(mat[i][j]);
                         j=j-data[i-1].first;
                        }
                }
         
                    
        for(int i=1;i<sequence.size();i++)
            cout<<sequence[i]<<"\t";



    }

};

int main()
{
    cutting_rod r;
    r.compute();
    return 0;
}

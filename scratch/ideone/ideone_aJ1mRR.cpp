#include<iostream>
#include<vector>
#include<limits.h>
#include<tgmath.h>
#include<algorithm>
using namespace std;

class bit
{

vector<string> mat;
   public:
        void initial()
       {   int row,col,no_of_matrix;
           string input,temp;
            cin>>row;
            cin>>col;
            cin>>no_of_matrix;

            for(int i=0;i<no_of_matrix;i++)
            {    input="";
            for(int j=0;j<row;j++)
                 {temp="";
                     cin>>temp;
                    input=input+temp;
                }
                 mat.push_back(input);
            }
        if(mat.empty())
				return;
        }
int supplement(vector<int> &res)
       {

    int  x = 0;

    for(int i = 0;i < mat.size() ;i++)
    {   for(int j = i+1; j < mat.size();j++)
            {   x= 0;
                for(int k = 0 ; k < res.size(); k++)
                    {     if(mat[i][res[k]] != mat[j][res[k]])
                          x++;
                    }
                if(x == 0)
                {    return x;
                }
            }
    }
    return 1;
}

void compute()
{    int option;
    int sz= ceil(log2(mat.size()));
    int temp=sz;
    while( temp< mat.size())
        {     string comp(temp, 1);
              comp.resize(mat[0].size(), 0);
         do {   vector<int> check;
                int z=0;
                while(z < mat[0].size())
                    {   if (comp[z]){
                            check.push_back(z);
                    }
                z++;
            }
            option=supplement(check);
            if(option)
                 {   cout<<temp;
                     return;
                 }
        } while (prev_permutation(comp.begin(), comp.end()));
    temp++;
    }

}


};

int main()
{   bit b;
    b.initial();
    b.compute();
return 0;
}


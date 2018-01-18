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
        bool supplement(vector<int> &res)
        {   int  temp;
    for(int i = 0;i < mat.size() ;i++)
        {   for(int j = i+1; j < mat.size() ;j++)
                {   temp =  0;
                    for(int k = 0 ; k < res.size(); k++)
                        {   if(mat[i][res[k]] != mat[j][res[k]])
                            temp++;
                        }
                if(temp== 0)
                    return true;
                }
        }
    return false;
}
  void initial()
       {   int row,col,no_of_matrix;
           string input,temp;
            cin>>row;
            cin>>col;
            cin>>no_of_matrix;

            for(int i=0;i<no_of_matrix;i++)
            {   for(int j=0;j<row;j++)
                 {  cin>>input;
                    input=input+temp;
                }
                 mat.push_back(input);
            }
        if(mat.empty())
				return;
        }

  void compute()
    {
    vector<int> res;
    int min_bit = INT_MAX;
    int len = mat[0].size();
    int cell = ceil(log2(mat.size()));
    int temp=cell;
    int temp2=0;

    while(temp< mat.size())
        {   string comp(temp, 1);
            comp.resize(len, 0);
            do {    while(temp2 < len)
                    {   if (comp[temp2])
                        {   res.push_back(temp2);
                        }
                temp2++;
                    }
                int dec=supplement(res);
                if(dec)
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


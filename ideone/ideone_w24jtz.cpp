#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
typedef pair<int,pair<int,int> > o;

bool cmp(const pair<int,pair<int,int>> &a, const pair<int,pair<int,int>> &b)
    {   
        return a.second.second<b.second.second;
    
    }


class Graph{
    vector<o> p;
   long sum;
    int v;
    vector<int>parent;
    
    public:
    Graph(int v)
        {       this->v=v;
                parent.resize(v,-1);      }
    
    void addEdge(int u,int v,int w)
        {   p.push_back(make_pair(u,make_pair(v,w)));
        }
    
    int find( int v)
        {   if(parent[v]==-1)
                 return v;
       
         return find(parent[v]);
         }
    
    void uniona(int v,int u)
        {   int x=find(u);
             int y=find(v);
             parent[x]=y;
       }
    
    int cycle(int u, int v)
        {   int x,y;
            x=find(u);
            y=find(v);
         
         if(x==y)
             return 1;
         
         uniona(x,y);
           return 0;
     }
    
    void compute()
        {   sort(p.begin(),p.end(),cmp);
         sum=0;   
         int e=0;
         int i=0;
         pair<int,pair<int,int> > temp;
         while(e<v-1)
             {  temp=p[i++];
                int u=temp.first;
                 int v=temp.second.first;
                 int wt=temp.second.second;
           
              if(!cycle(u,v))
                        {   sum=sum+wt;
                                     e++; }

                         }
         cout<<sum;
        
    }
    
};

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n,x,y,z,s,e;
    cin>>n>>e;
    int temp=e;
      // cout<<n;
     Graph g(n);    
   
    while(temp)
        {   cin>>x>>y>>z;
      
            g.addEdge(x,y,z);
         // cout<<temp;
         temp--;
        }
   
        g.compute();
    return 0;
}
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
typedef pair<int,pair<int,unsigned long > > o;

bool cmp(const pair<int,pair<int,unsigned long >> &a, const pair<int,pair<int,unsigned long >> &b)
    {   
        return a.second.second<b.second.second;
    
    }


class Graph{
    vector<o> p;
   unsigned long sum;
    int v;
    vector<int>visit;
    vector<int>parent;
    
    public:
    Graph(int v)
        {       this->v=v;
                visit.resize(v+1,0);  
                parent.resize(v+1,-1);    
        }
    
    void addEdge(int u,int v,unsigned long w)
        {   p.push_back(make_pair(u,make_pair(v,w)));
        }
    
    int find(int v)
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
         int i=0,j;
         pair<int,pair<int,unsigned long > > temp,it;
         while(e<v-1&&i<p.size())
             {  temp=p[i++];
                int u=temp.first;
                 int v=temp.second.first;
                 unsigned long  wt=temp.second.second;
           
              if(!cycle(u,v))
                        {   sum=sum+wt;
                        e++;
                        visit[u]=1;
                        visit[v]=1;
                         
                         j=i+1;
                         while(j<p.size())
                             {  it=p[j];
                                 if((it.first==u&&it.second.first==v)||(it.first==v&&it.second.first==u))
                                     {   p.erase(p.begin()+j);
                                     j=0;
                                     }
                             j++;
                            }
                        }
                 }
                         
         cout<<sum;
        
    }
    
};

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n,x,y,s,e;
    cin>>n>>e;
    int temp=e;
      // cout<<n;
     Graph g(n);  
    unsigned long z;
   
    while(temp)
        {   cin>>x>>y>>z;
      
            g.addEdge(x,y,z);
         // cout<<temp;
         temp--;
        }
   
        g.compute();
    return 0;
}
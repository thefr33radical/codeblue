#include <cmath>
#include<bits/stdc++.h>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


class prims
    {   list<pair<int,int> > *adj;
        int v;
     
     public:
     prims(int x)
         {  this->v=x;
            adj=new list<pair<int,int> >[v];
         }
    
     void add(int v1,int v2,int w)
         {  adj[v1].push_back(make_pair(v2,w));
            adj[v2].push_back(make_pair(v1,w)); 
          cout<<"1 ";
         }
     
     void compute(int s)
         {  vector<int>vis(v,0);
            vector<int>dis(v,999);
            vector<int>parent(v,-1);
          
            priority_queue<pair<int,int>,vector<pair<int,int> >,greater<pair<int,int> > >q;  
            
            q.push(make_pair(0,s));
          int u,v,wt;
          while(!q.empty())
              {  pair<int,int> temp=q.top();
                  u=temp.second;
                       
                    vis[u]=1;
                  for(auto it=adj[u].begin();it!=adj[u].end();it++)
                    {   v=it->second;
                        wt=it->first;
                        
                        if(wt<dis[v]&&vis[v]==0)
                            {   //vis[v]==1;
                                parent[v]=u;
                                dis[v]=wt;
                            cout<<"\n"<<u<<" "<<v<<"\n";
                                q.push(make_pair(wt,v));
                           }
                    }
                }
          int sum=0;
          for(auto it:dis)
              sum=sum+(it);
            cout<<sum;
         }
    
};


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n,x,y,z,s,e;
    cin>>n>>e;
    int temp=e;
       cout<<n;
     prims *g; 
     g=new prims(n);
    
    while(temp)
        {   cin>>x>>y>>z;
         cout<<x<<y<<z<<"\n";
         //   g->add(x,y,z);
          cout<<temp;
          temp--;
        }
  // cin>>s;
    cout<<"asdasd";
    cout<<s;
        g->compute(s);
    return 0;
}

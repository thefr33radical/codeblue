#include<bits/stdc++.h>
using namespace std;
typedef pair<int,int> o;

class Graph
    {   int v;
        list <o>*adj;
        
     
     public:
     
     Graph(int v)
         {  this->v=v;
            adj=new list<o>[v+1];
         }
     void addEdge(int u,int v,int w)
         {  adj[u].push_back(make_pair(v,w));
            adj[v].push_back(make_pair(u,w));
         }
     void prims(int src)
         {  vector<unsigned long>dist(v+1,999999);
            vector<int>visit(v+1,0);
            vector<int>parent(v+1,-1);
            priority_queue<pair<int,int>,vector<o>,greater<o>> q;
          dist[src]=0;
          visit[src]=1;
unsigned long sum=0;
          
          q.push(make_pair(0,src));
          
          while(!q.empty())
              {     pair<int,int> temp=q.top();
                    q.pop();
                    int u=temp.second;
//int s=temp.first;
                  visit[u]=1;
//cout<<u<<"\t";
               for(list<o>::iterator it=adj[u].begin();it!=adj[u].end();it++)
                   {    int v=it->first;
                        unsigned long wt=it->second;
cout<<v<<"\t";
                        if(!visit[v]&&wt<dist[v])
                            {   q.push(make_pair(wt,v));
                                parent[v]=u;
                                dist[v]=wt;
                           //    sum=sum+s;
                            }
                    }
                }
cout<<"\n";
          for(int i=1;i<dist.size();i++)
              {    cout<<dist[i]<<"\t";
              		if(dist[i]!=999)
              			sum=sum+dist[i];
                  
                    }
          cout<<sum;
            }
    
    
    };

int main()
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n,x,y,z,s,e;
    cin>>n>>e;
    int temp=e;
      // cout<<n;
     Graph g(n);    
   
    for(int i=0;i<e;i++)
        {   cin>>x>>y>>z;
            g.addEdge(x,y,z);
//cout<<x<<y<<z;
        }
    cin>>s;
   //cout<<"\n"<<s;
//  
g.prims(s);
    return 0;
}

// use bfs and indegree approach

#include<bits/stdc++.h>

class kahns
{

int v;
list <int> *adj;
vector <int> indegree;
public:

    kahns(int v)
    {
        this->v=v;
        adj=new list<int>[v];
        indegree(v,0);
    }

    void add_edge(int v1,int v2)
    {
        adj[v1].push_back(v2);
        indegree[v2]++;
        adj[v2].push_back(v1);
        indegree[v1]++;
  }






};


int main()
{

kahns k(2);


    return 0;
}


#include <algorithm>
#include <iostream>
#include <string>
#include <functional>
#include<bits/stdc++.h>

using namespace std;

class graph
{
    int vertex;
    list <int> *adj;

    public:
        graph(int v )
        {
            this->vertex=v;
            adj=new list<int>[v];

        }

        void addEdge(int vertex, int connect_with)
        {
            adj[vertex].push_back(connect_with);

        }

        void BFS(int node)
        {
            int i,pr;
            bool *visited=new bool[vertex];
            list<int>::iterator x;
            list<int>q;



            for(int i=0; i<vertex;i++)
                {
                    visited[i]=false;
                }

            visited[node]=true;
            q.push_back(node);

            while(!(q.empty()))
                {
                    pr=q.front();
                    cout<<pr<<"\n";
                    q.pop_front();


            for(x=adj[node].begin();x!=adj[node].end();x++)
            {
                if(!visited[*x])
                {
                visited[*x]=true;
                    q.push_back(*x);

                }

                }

            }




        }



};

int main()
{
graph g(4);

g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 0);
    g.addEdge(2, 3);
    g.addEdge(3, 3);

    cout << "Following is Breadth First Traversal (starting from vertex 2) \n";
    g.BFS(2);

return 0;
}

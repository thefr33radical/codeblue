#include <iostream>
#include<bits/stdc++.h>
using namespace std;

class Graph
{	int v;
	list<int> *adj;
	vector<int> indegree;
	
public:
	Graph(int nodes)
		{	this->v=nodes;
			adj=new list<int>[nodes];		
			for(auto i=0;i<v;i++)
			  indegree.push_back(0);
		}
	
	void addEdge(int u, int v)
	{
		adj[u].push_back(v);
		indegree[v]++;
	}
	
	void compute()
	{	queue<int> q;
		
		for(int i=0;i<indegree.size();i++)
		{	if(indegree[i]==0)
				{	q.push(i);
					
				}
		}
		int cnt=0;
		list<int>::iterator i;
		while(!q.empty())
		{	
			int n=q.front();
			cout<<n<<" ";
			q.pop();
			cnt++;
			for(i=adj[n].begin();i!=adj[n].end();i++)
				{	indegree[*i]--;
					if(indegree[*i]==0)
						q.push(*i);
					
				}
		}
		
		if(cnt!=v)
			cout<<"\n There exists a cycle";
	}
	
	
};






// Driver program to test above functions
int main()
{
    // Create a graph given in the above diagram
    Graph g(6);
    g.addEdge(5, 2);
    g.addEdge(5, 0);
    g.addEdge(4, 0);
    g.addEdge(4, 1);
    g.addEdge(2, 3);
    g.addEdge(3, 1);
 
    cout << "Following is a Topological Sort of\n";
    g.compute();
 
    return 0;
}
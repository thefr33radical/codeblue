//DFS Practice
// Directed graph


#include <iostream>
#include<bits/stdc++.h>
using namespace std;

class dfs
{	list<int> *adj;
	int nodes;
	
	public:
	
	dfs(int m);
	void insert(int u,int v);
	void dfser(int s, vector<bool> &visit);
	void compute(int s);	
};

dfs::dfs(int m)
{	adj=new list<int>[m];
	this->nodes=m;
}

void dfs::insert(int u,int v)
{	adj[u].push_back(v);
	
}

void dfs::dfser(int s,vector<bool> & visit)
{	cout<<s<<" ";
	visit[s]=true;
	for(auto i=adj[s].begin();i!=adj[s].end();i++)
	{		if(visit[*i]==false)
			{	dfser(*i,visit);
				
			}
	}
}

void dfs::compute(int s)
{	vector<bool> visit(nodes,false);
	
	for(auto i=adj[s].begin();i!=adj[s].end();i++)
	{		if(visit[*i]==false)
			{	dfser(*i,visit);
				
		
			}
	}
}

int main() {
	
	// y // Create a graph given in the above diagram
    dfs g(4);
    g.insert(0, 1);
    g.insert(0, 2);
    g.insert(1, 2);
    g.insert(2, 0);
    g.insert(2, 3);
    g.insert(3, 3);
 
    cout << "Following is depth First Traversal "
         << "(starting from vertex 2) n";
    g.compute(2);//our code goes here
    return 0;
}
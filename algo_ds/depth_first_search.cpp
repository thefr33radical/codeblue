#include <iostream>
#include<bits/stdc++.h>
using namespace std;

// Directed unweighted graph

class graph{
list<int> *adj;
int vertex;
public:
graph(int);
void add_edge(int ,int);
void dfs(int);
void dfs2(int,vector<bool>&visited);
};

graph::graph(int v)
{	vertex=v;
	adj=new list<int> [vertex];
}

void graph::add_edge(int u , int v)
{
	adj[u].push_back(v);
}

void graph::dfs(int src)
{
	vector<bool> visited(vertex,false);
	cout<<src<<"\n";
	visited[src]=true;
	for(auto i=adj[src].begin();i!=adj[src].end();i++)
	{	
		if(visited[*i]==false)
		{	visited[*i]=true;
			cout<<*i<<"\n";
			dfs2(*i,visited);
		}
	}
	
}

void graph::dfs2(int start,vector<bool> &visited)
{
	
		for(auto i=adj[start].begin();i!=adj[start].end();i++)
	{	
		if(visited[*i]==false)
		{	visited[*i]=true;
			cout<<*i<<"\n";
			dfs2(*i,visited);
		}
	}
	
	
}


int main() {
	// your code goes here
	
	graph g(7);
	// 0 egde is unfilled so use n+1 vertices  for vertex array
	
	g.add_edge(1,4);
	g.add_edge(4,5);
	g.add_edge(5,6);
	g.add_edge(1,2);
	g.add_edge(1,3);
	g.add_edge(2,3);
	g.add_edge(3,4);
	g.dfs(1);
	
	return 0;
	
}

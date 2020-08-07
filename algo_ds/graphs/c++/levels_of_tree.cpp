#include <iostream>
#include<bits/stdc++.h>
using namespace std;



void printLevels(vector<int> &graph,int v,int src)
{
	queue<make_pair<int,int>>q;
	int count=0;
	q.push(make_pair<src,0>);

	while(!q.empty())
	{	int vertex=q.front();
		q.pop();
		count++;
		for(auto i=graph[vertex].begin();i!=graph[vertex].end();i++)
		{
			q.push(make_pair<*i,count>);

		}
	for(i:q)
	{
		cout<<i.first<<i.second;
	}

	}



}



int main()
{
    // adjacency graph for tree
    int V = 8;
    vector<int> graph[V];

    graph[0].push_back(1);
    graph[0].push_back(2);
    graph[1].push_back(3);
    graph[1].push_back(4);
    graph[1].push_back(5);
    graph[2].push_back(5);
    graph[2].push_back(6);
    graph[6].push_back(7);

    // call levels function with source as 0
    printLevels(graph, V, 0);

    return 0;
}

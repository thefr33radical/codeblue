//Directed BFS

#include <iostream>
#include<bits/stdc++.h>
using namespace std;

class bfs
{	list<int> *nodes;
	int m;
public:	
	bfs(int m);
	void addEdge(int m, int n);
	void compute(int n);
};

void bfs::addEdge(int m, int n)
{	nodes[m].push_back(n);
}

bfs::bfs(int m)
{	nodes=new list<int>[m];
		this->m=m;
}
	
void bfs::compute(int n)
{	queue<int> q;
	vector <bool> visit(n,false);
	
	visit[n]=true;
	q.push(n);
	int temp;
	
	while(!q.empty())
	{	temp=q.front();
		q.pop();
		cout<<temp<<" ";
		
		for(auto i=nodes[temp].begin();i!=nodes[temp].end();i++)
		{	if(visit[*i]==false)
			{	q.push(*i);
				visit[*i]=true;
				
			}
			
		}
		
	}
	
	
	
	
}
	

int main() {
	// y // Create a graph given in the above diagram
    bfs g(4);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 0);
    g.addEdge(2, 3);
    g.addEdge(3, 3);
 
    cout << "Following is Breadth First Traversal "
         << "(starting from vertex 2) n";
    g.compute(2);//our code goes here
	return 0;
}
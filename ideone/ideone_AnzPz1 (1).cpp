#include <iostream>
#include<bits/stdc++.h>
using namespace std;


class graph
{	
		public:
		int mat[12][12] =
	{
		{ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 },
		{ 1, 0, 1, 1, 1, 1, 1, 1, 1, 1 },
		{ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 },
		{ 1, 1, 1, 1, 0, 1, 1, 1, 1, 1 },
		{ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 },
		{ 1, 1, 1, 1, 1, 0, 1, 1, 1, 1 },
		{ 1, 0, 1, 1, 1, 1, 1, 1, 0, 1 },
		{ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 },
		{ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 },
		{ 0, 1, 1, 1, 1, 0, 1, 1, 1, 1 },
		{ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 },
		{ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 }};
	
	int min_path;
	map<string,int>visited;
		map<string,bool>bomb;
	vector<int>path[12];
	graph()
	{
		this->min_path=0;
		
	}
	void mbfs(int i,int j,int path)
	{
		int node=mat[i][j];
		string temp=to_string(i);
		temp=temp+to_string(j);
		path=path+1;
		
		
		
		cout<<"\n I am here "<<temp;
		if(!bomb.count(temp)) // check if bomb co-ordinate
		{
			bomb[temp]=1;
			
				cout<<"\n I am here "<<;
			if(node==0)//mark all surroung co-ordinates as bomb co ordisnates
			{
				int p=-1;
				while(p<2)
				{
					int q=-1;
					string addbmb="";
					while(q<2)
					{	
						int px=i+p;
						int qx=j+q;
						
						if(px>-1&&qx>-1&&px<12&&qx<12)
						{
						addbmb+=to_string(px);
						addbmb+=to_string(qx);
						
						bomb[addbmb]=true;
						cout<<bomb[addbmb];
						}
						q++;
					}
					p++;
				}
				visited[temp]=true;
			return ;	
			}
		}
		
		else
		{
			if(!visited(temp.count))
			{	path[mat[i][j]]=path;
				
				q.push(make_pair(i,j+1);//left
				q.push(make_pair(i+1,j);//bottom
				q.push(make_pair(i-1,j);
				q.push(make_pair(i,j-1);
				
				while(!q.empty())
				{
					pair<int, int> store=q.front();
					int u=store->first;
					int v=store->second;
				mbfs(u,v,path);	
				}
				
				
				if(visited(temp.count)&&path<path_mat[i][j])
				{
					path[mat[i][j]]=path;
				
				q.push(make_pair(i,j+1);//left
				q.push(make_pair(i+1,j);//bottom
				q.push(make_pair(i-1,j);
				q.push(make_pair(i,j-1);
				
				while(!q.empty())
				{
					pair<int, int> store=q.front;
					int u=store->first;
					int v=store->second;
				mbfs(u,v,path);	
				}
				
				
				
			}
				
				
				
			}
			
			return;
			
			
			
		}
		
		
		
		
	}
	
};



int main() {
	// input matrix with landmines shown with number 0
	graph g;
	g.mbfs(0,1);

	return 0;
	}
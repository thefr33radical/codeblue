#include<bits/stdc++.h>
using namespace std;
int main()
{
	int c,n,m;
	cin>>m>>n>>c;
	int matrix[c+1][n+1][m+1]; // x,y,z such that xth 2D matrix represnt xth character
	for(int i=1;i<=c;i++)
	{
		for(int j=1;j<=m;j++)
		{
			for(int k=1;k<=n;k++)
			{
				cin>>matrix[i][j][k];
			}
		}
	}
	bool compared[100][100] = {0};
	vector<set<pair<int,int > > > V;
	for(int i=1;i<=c;i++)
	{
		for(int j=1;j<=c;j++)
		{
			if(i!=j && !compared[i][j] && !compared[j][i])
			{
				set<pair<int,int > > S;
				compared[i][j] = compared[j][i] = 1;
				for(int x=1;x<=m;x++)
				{
					for(int y=1;y<=n;y++)
					{
						if(matrix[i][x][y] != matrix[j][x][y])
						{
							S.insert(make_pair(x,y));
						}
					}
				}
				V.push_back(S);
			}
		}
	}
	map<pair<int,int>,int> M; // for keeping record that a point x,y exists in how many comparisions
	bool included[100];
	memset(included,0,sizeof(included));
	bool done = 0;
	int ans = 0;
	while(!done)
	{
		for(int i=0;i<V.size();i++)
		{
			if(!included[i])
			for(auto it = V[i].begin();it!=V[i].end();it++)
			{
				M[*it]++;
			}
		}
		int maxi = 0;
		pair<int,int> P;
		for(auto it = M.begin() ; it!=M.end() ; it++)
		{
			if(it->second > maxi)
			{
				P = it->first;
				maxi = it->second;
			}
		}
		for(int i=0;i<V.size();i++)
		{
			if(!included[i] && V[i].find(P)!=V[i].end())
			{
				included[i] = 1;
				V[i].erase(P);
			}
		}
		ans++;
		int i;
		for(i=0;i<V.size();i++)
		{
			if(!included[i])
			{
				break;
			}
		}
		if(i==V.size())
		{
			done = 1;
		}
		M.clear();
	}
	cout<<ans<<endl;
	return 0;
}

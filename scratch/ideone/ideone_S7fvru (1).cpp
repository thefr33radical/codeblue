#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<map>
using namespace std;


int main() {
    
   int n;
    string temp;
    vector<string> str;
    
    map<char,int> m;
  // vector<map<char,int>> store;
   
    cin>>n;
    int x=n;
    int min=0,mazx=999,index;
     vector<map<char,int>> store;
     //store=new  vector<map<char,int>>[n];
  
    while(n--)
        {
        cin>>temp;
        str.push_back(temp);
        }
    
    for(int i=0;i<str.size();i++)
    {	int m_min=str[i].size();
    	if(min>m_min)
    	{min-m_min;
    		index=i;
    	}
    	for(int j=0;j<str[i].size();j++)
    	{
    	//	m[str[j]]++;
    	m[str[i][j]]++;
    	}
    	store.push_back(m);
    		m.clear();
    
    }/* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}

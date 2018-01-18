#include <iostream>
#include<bits/stdc++.h>
using namespace std;

class trie
{	public:
	class node
	{	public:
		node *kids;	
		bool isleaf;
		node()	
		{	kids=new node[26];
			for(auto i=0;i<26;i++)
			 //  kids[i]=NULL;
			isleaf=false;
		}
	};
	
	
	void insert(node *head,string str)
	{	
		node *temp=head;
		int length=str.size();
		int index;
		
		for(int i=0;i<length;i++)
		{	index=str[i]-'a';
			if(!temp->kids[index])
				temp->kids=new node();
			else
				temp=temp->kids[index];
				
			
		}
		temp->isleaf=true;
	}
	
	
};


int main() {
	// your code goes here
	return 0;
}
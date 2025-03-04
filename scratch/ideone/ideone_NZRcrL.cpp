#include <iostream>
#include<bits/stdc++.h>
using namespace std;


int main() {
	//code
	int inp;
	int l1,l2;
string str1,str2;
	cin>>inp;
	
	while(inp)
	{
	cin>>l1;
	cin>>l2;
	cin>>str1;
	cin>>str2;
	
	vector<string> v(l1+l2);  
	
	sort(str1.begin(),str1.end());
	sort(str2.begin(),str2.end());
	
vector<	string>::iterator it;
	
	it=set_intersection(str1.begin(),str1.end(),str2.begin(),str2.end(),v.begin());
	v.resize(it-v.begin());
	for (it=v.begin(); it!=v.end(); ++it)
    std::cout << ' ' << *it;
	inp--;
	cout<<endl;
	}
	
	
	return 0;
}
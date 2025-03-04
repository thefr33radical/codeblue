#include <cmath>
#include<map>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
	
	string str;
	map<char,int> z;
	
	getline(cin,str);
	
	for(int i=0;i<str.size();i++)
	{
		if(isalpha(str[i]))
		z[str[i]]++;
	}
	
	i
	
	cout<<str<<z.size();
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    return 0;
}

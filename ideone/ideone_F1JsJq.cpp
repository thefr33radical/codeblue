//Project Euler Problem 1

#include <iostream>
using namespace std;

int main() {
	long long sum=0;
	// your code goes here
	for(auto i=3;i<1000;i++)
	{	if(i%3==0||i%5==0)
		{	sum=sum+i;
		
		}
	}
	cout<<sum;
	
	return 0;
}
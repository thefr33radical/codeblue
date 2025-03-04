#include <iostream>
using namespace std;

int add(int x,int y)
{
	while(y)
	{	
		int carry=x&y;
		x=x^y;
		y=carry<<1;
	}
return x;	
}

int main() {
	// your code goes here
	
	cout<<add(5,9);
	return 0;
}
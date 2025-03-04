#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int a[]={1,2,3,4,5,7,8,16,9};
	int key;
	
	for(int i=1;i<9;i++)
	{
		key=a[i];
		int j=i-1;
		while(j>=0&&key<a[j])
		{	a[j+1]=a[j];
			j--;
			
		}
		a[j+1]=key;
//	cout<<a[i]<<"\t";
	}
	
	
	for(auto i=0;i<9;i++)
		cout<<a[i]<<"\t";
	
	
	
	
	
	
	return 0;
}
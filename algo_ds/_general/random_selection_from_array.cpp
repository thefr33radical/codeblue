#include <iostream>
#include<stdlib.h>
using namespace std;

int main() {
//	srand((int)time(0));
	
	int arr[]={1,34,32,67,75,45,99,23,556};
	int key=12;
	
	int n=(sizeof(arr)/sizeof(int))-1;
	int len=n;
	cout<<n;
	int i=0;
	for(;i<len;i++)
	{
		 n=rand()%len+1;
		 
	 if(key==arr[n])
	 {
	 	cout<<"found element";
	 }
	else
	{
		if(len>=0)
		{			 cout<<"\n array swap"<<arr[i]<<arr[n]<<"\n  "<<i<<n;
		 int temp =arr[n];
		 arr[n]=arr[len];
		 arr[len]=temp;
		 len=len-1;
		 i=0;
		 cout<<"\n length"<<len;
		
		 
			
		}
	}
	}


	return 0;
}

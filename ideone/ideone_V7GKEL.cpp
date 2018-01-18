#include <iostream>
using namespace std;

// Radix Sort
#include <iostream>
using namespace std;

int getmax(int arr[],int size)
{	int max=arr[0];
	for(int i=1;i<size;i++)
	{	if(arr[i]>max)
			max=arr[i];

	}
	return max;
}


void count_sort(int arr[],int exp,int size)
{
	int count[10]={0};
	int output[size];
	
	
	for(int i=0;i<size;i++)
		count[(arr[i]/exp)%10]++;
		
	for(int i=1;i<10;i++)
	{	count[i]+=count[i-1];
		}
	for(int i=size-1;i>=0;i--)
	{	output[count[(arr[i]/exp)%10]-1]=arr[i];
		count[(arr[i]/exp)%10]--;
		
	}
	
	for(int i=0;i<size;i++)
		arr[i]=output[i];
	
	
}


void sort(int arr[],int size)
{	int max=getmax(arr,size);
	for(int i=1;max/i>0;i=i*10)
		count_sort(arr,i,size);
}


int main() {
	// your code goes here
	
	int arr[]={10,2,33,4,5,6,7,78,3,1,78,90,111};
	int size=sizeof(arr)/sizeof(arr[0]);
	cout<<(size)<<"dasd";
	
	sort(arr,size);
	for(auto i:arr)
		cout<<i<<" ";
	return 0;
	
}


// Radix Sort

#include <iostream>
using namespace std;

int getmax(int arr[],int n)
{	int max=arr[0];
	for(int i=0;i<n;i++)	
		if(arr[i]>max)
			max=arr[i];
			
	return max;
}

void count_sort(int arr[],int n, int exp)
{	int count[10]={0};
	int output[n];
	
	for(int i=0;i<n;i++)
		count[(arr[i]/exp)%10]++;
		
	for(int i=1;i<10;i++)
		count[i]+=count[i-1];
		
	for(int i=n-1;i>0;i--)
		{	output[count	[(arr[i]/exp)%10 ]-1	]=arr[i];
			count[(arr[i]/exp)%10]--;
			}
	
	for(int i=0;i<n;i++)
		arr[i]=output[i];
	
}

void radix_sort(int arr[],int n)
{	int max=getmax(arr,n);
	for (int i=1; (max/i)>0; i=i*10)
		count_sort(arr,n,i);
}

int main() {
	// your code goes herent 
	
	int arr[] = {170, 45, 75, 90, 802, 24, 2, 66};
	int n=sizeof(arr)/sizeof(arr[0]);
	
	radix_sort(arr,n);
	
	cout<<"\n The Sorted array is :";
	
	for(auto i:arr)
		cout<<i<<" ";
		
	return 0;
}
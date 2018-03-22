#include <iostream>
#include<bits/stdc++.h>
using namespace std;

class qs
{

	public:
	vector<int> arr;
	void part(vector<int> &arr,int low,int high)
	{	if(low<high)
		{ int pivot =search(arr,low,high);
			part(arr,low,pivot-1);
			part(arr,pivot+1,high);
		}

	}

	int search(vector<int>&arr, int low, int high)
	{
		int i=low+1;
		int j=high;
		int temp;
		int p=arr[low];
		while(1)
		{	while(arr[i]<p)
			i+=1;
			while(arr[j]>=p)
			j+=1;

			if(i<j)
			{	temp=arr[i];
				arr[i]=arr[j];
				arr[j]=temp;
			}
			else
				break;
		}

		arr[low]=arr[i];
		arr[i]=p;

		return i;
	}

};



int main() {
#include <iostream>
#include<bits/stdc++.h>
using namespace std;

class qs
{

    public:

	vector<int> part(vector<int> &arr,int low,int high)
	{	if(low<high)
		{ int pivot =search(arr,low,high);
           // cout<<"\n"<<pivot<<"\n";
			part(arr,   low,pivot-1);
			part(arr,pivot+1,high);
		}
	//	cout<<"\n";
	//	for(int i=0;i<arr.size();i++)
     //       cout<<arr[i]<<" ";
     // cout<<"\n";
        return arr;
	}

	int search(vector<int>&arr, int low, int high)
	{
		int i=low+1;
		int j=high;
		int temp;
		int p=arr[low];

		while(1)
		{	while(i<j &&arr[i]<=p) //  both the conditions are critical
			i++;
			while(arr[j]>=p && j>=i) //  both the conditions are critical
			j--;

			if(i<= j)
			{	temp=arr[i];
				arr[i]=arr[j];
				arr[j]=temp;
				i++;
				j--;
			}
			else if(i>=j)
				break;
		}

		arr[low]=arr[j];
		arr[j]=p;
        cout<<arr[j]<<"\t "<<i;
        cout<<"\n";
		return j;
	}// return j rightmost val

};



int main() {
    int a[]={2,34,12,45,6,3,76,8};
	vector<int>ar(a,a + sizeof(a) / sizeof(int));
	qs *t=new qs();
	ar=t->part(ar,0,ar.size()-1);
    for(int i=0;i<ar.size();i++)
        cout<<ar[i]<<" ";

	// your code goes here
	return 0;
}

	vector<int>arr={2,34,12,45,6,3,76,8};
	qs *a=new qs();
	a->part(arr,0,arr.size()-1);

	// your code goes here
	return 0;
}

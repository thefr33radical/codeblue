// implementation of randomized quick sort using STL
// TC= O(nlogn) --> O(n)2


#include<bits/stdc++.h>
#include<cstdlib>
using namespace std;

int picker(vector<int>&arr,int low,int high)
{
    int r=(rand()%(high -low))+low;
    int temp=arr[r];
    arr[r]=arr[low];
    arr[low]=temp;

    int pivot =arr[low];

    int i=low+1;
    int j=high;

    while(1)
    {   while(arr[i]<pivot && i<high)
            i++;
        while(arr[j]>pivot && j>low)
            j--;

        if(i<j)
            {   int temp=arr[i];
                arr[i]=arr[j];
                arr[j]=temp;
            }
        else
              break;
     }

     arr[low]=arr[j];
     arr[j]=pivot;
     return j;

}

void partitioner(vector<int>&arr,int low,int high)
{   if(low<high){
    int pivot=picker(arr,low,high);
    partitioner(arr,low,pivot-1);
    partitioner(arr,pivot+1,high);
    }

}


int main()
{
    int a[]={2,4,5,71,45,8};
    vector<int> arr(a,a+sizeof(a)/sizeof(int));
    partitioner(arr,0,arr.size()-1);
    for(i:arr)
    cout<<i<<" ";

return 0;
}

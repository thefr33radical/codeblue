// implementation of randomized quick sort using STL
// TC= O(nlogn) --> O(n)2



#include<bits/stdc++.h>
using namespace std;

int sorter(vector<int>&arr,int low,int high)
{   int pivot=arr[low];
    int i=low+1;
    int j=high;

    while(1)
    {   while(arr[i]<pivot && i <= j)
        i++;
        while(arr[j]>=pivot && j>=i)
        j--;

        if(i<j)
        {   int temp=arr[i];
            arr[i]=arr[j];
            arr[j]=temp;
      }
      if(i>=j)
        break;
    }
    arr[low]=arr[j];
    arr[j]=pivot;
    return j;

}


void compute(vector<int>&arr,int low,int high)
{   //int pivot=0;
    if(low<high)

    {   int pivot=sorter(arr,low,high);
        compute(arr,low,pivot-1);
        compute(arr,pivot+1,high);
   }
}

int main()
{   int a[]={2,4,5,71,45,8};
    vector<int> arr(a,a+sizeof(a)/sizeof(int));
    compute(arr,0,arr.size()-1);
    for(i:arr)
    cout<<i<<" ";
return 0;
}

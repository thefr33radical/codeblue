
//Practice : Randomized quick sort
#include<bits/stdc++.h>
using namespace std;

int qs(vector<int>&arr,int low,int high)
{
    int r=(rand()% (high-low))+low;
    int temp=arr[r];
    arr[r]=arr[low];
    arr[low]=temp;

    int i=low+1;
    int j=high;

    int pivot=arr[low];

    while(1)
    {
        while(arr[i]<pivot && i<j)
               i++;

         while(arr[j]>=pivot && j>=i)
               j--;

        if(i<j)
            {   int temp= arr[i];
                arr[i]=arr[j];
                arr[j]=temp;

            }

         if(i>=j)
            break;

     }

     temp= arr[j];
     arr[j]=pivot;
     arr[low]=temp;

    return j;


}

void part(vector<int>&arr,int low, int high)
{
    if(low<high)
    {
        int pivot=qs(arr,low,high);
        part(arr,low,pivot-1);
        part(arr,pivot+1,high);



    }




}

int main()
{
vector<int>arr={2,34,12,45,6,3,76,8};
part(arr,0,arr.size());

for(auto i:arr)
    cout<<i<<"\t";
return 0;
}

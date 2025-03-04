
#include<bits/stdc++.h>
using namespace std;
void sorter(vector<int>&arr,int low, int mid,int high)
{
    int start1=low;
    int start2=mid+1;
    vector<int>temp;
//cout<<"fff";

    while(start1<=mid && start2<=high)
    {
        while(arr[start1]<arr[start2])
                {temp.push_back(arr[start1]);
                start1++;

                }

        while(arr[start1]>=arr[start2])
                {temp.push_back(arr[start2]);
                    start2++;
                }
    }


    while(start1<=mid)
                {temp.push_back(arr[start1]);
                start1++;
                }
    while(start2<=high)
                {temp.push_back(arr[start2]);
                start2++;
                }

    int k=0;
    for(int i=low; i<=high;i++)
    {    cout<<temp[k];
            arr[i]=temp[k++];

    }
    temp.clear();
    cout<<"\n";


}




void merge_sort(vector<int>&arr,int low,int high)
{   if(low<high)
    {
        //cout<<"fff";

        int mid=(low+high)/2;
        merge_sort(arr,low,mid);
        merge_sort(arr,mid+1,high);
        sorter(arr,low,mid,high);

    }
}


int main()
{

    vector<int>arr={1,4,3,6,6,3,8,23,4};
     for(int i=0;i<arr.size();i++)
        cout<<arr[i]<<" ";

    cout<<"\n";
    merge_sort(arr,0,arr.size());

    for(int i=0;i<arr.size();i++)
        cout<<arr[i]<<" ";

    return 0;
}

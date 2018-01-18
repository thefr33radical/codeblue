#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    
    vector<int>arr,range,sum,count;
    int temp,max_ele,min_ele,inp;
    
    cin>>inp;
    while(inp--)
        {   cin>>temp;
            arr.push_back(temp);        //On(n)
        }
    
    min_ele=*min_element(arr.begin(),arr.end());     //On(n)
    max_ele=*max_element(arr.begin(),arr.end());     //O(N)
    
    for(auto i=0;i<max_ele;i++)
        {   range.push_back(0);
                   
        }
    for(auto i=0;i<arr.size();i++)
        {   range[arr[i]]++;
           // cout<<range[i];
        }
    
     for(auto i=min_ele;i<max_ele;i++)
        {  cout<<range[i]<<" ";
        
        }
    
    
    
    
    return 0;
}

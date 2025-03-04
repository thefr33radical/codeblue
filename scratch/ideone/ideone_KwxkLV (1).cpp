#include <iostream>
#include<bits/stdc++.h>
using namespace std;
bool cmp(const pair<long,long> &a,const pair<long,long> &b)
{
	return a.first<b.first;
}
int main()
{
	

   long n, t,sal1,sal2;
   cin>>n;
   t=n;
   //n=t;
   
   
   vector<pair<int ,int> > arr,arr1;
   while(t--)
   {
   	cin>>sal1>>sal2;
   	
   	arr.push_back(make_pair(sal1,sal2));
   	
   
   }
   
   arr1=arr;
 sort(arr.begin(),arr.end(),cmp);
   
  // for(auto it:arr)
  // cout<<it.first;
   
  long team_size=arr.size()/2;
  
  vector<long>res;
  
  	if(team_size%2!=0){
  	return 0; //team not possible
	}
	int j=arr.size();
  	long sum=arr[j].first;
  	sum=arr[j--].first+sum;
  	cout<<sum;
  	int i=0;
  	while(i<j)
  		{
  		sum=sum+(arr1[j].second)+(arr1[i].second);
  		i++;
  		j--;
  		}
  	
  cout<<sum;

	return 0;
	
}
   

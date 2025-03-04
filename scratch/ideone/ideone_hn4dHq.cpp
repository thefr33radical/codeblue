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
   n=t;
   
   
   vector<pair<long,long> > arr;
   vector<pair<long,long> > arr1;
  
   while(t)
   {
   	cin>>sal1>>sal2;
   //	cin>>sal2;
   	cout<< sal1;
   	arr.push_back(make_pair(sal1,sal2));
   	t--;
   cout<<sal1;
   cout<<sal2;
   }
   cout<<"dsfsd";
   arr1=arr;
 sort(arr.begin(),arr.end(),cmp);
   
  // for(int it=0; it<3;it++)
	// cout<<arr[it].first;
   
  long team_size=arr.size()/2;
  
  vector<long>res;
  
  	if(team_size%2!=0)
  	return 0; //team not possible
  	
  	long sum=0;
  	int j=team_size-1;
  	int i=0;
  	while(i<j)
  		{
  		sum=sum+(arr[i].first)+(arr[j].second);
  		i++;
  		j--;
  		}
  	
  cout<<sum;

	return 0;
	
}
   

//using the concept of N!/(R!*(N-R)!)




#include<iostream>

using namespace std;


int compute_factorial(int val)
{
  
  int i;
 if(val==0 || val==1)
   return 1;
 
for(i=val-1;i>=1;i--)
{ val=val*i;
  
}
return val;
  
}




int main()
{
  
  int x,y,p,i,j,k,set=1;;
  cout<<"Enter the number of lines : ";
  cin>>x;
  
  
  for(i=0;i<x;i++)
  {
    set=1;
    for(j=0;j<=i;j++)
    {
      if(set==1)
      {
      for(k=0;k<(x/2)-i;k++)
      {
	cout<<"\t";
	set=0;
      }
      }
    p= compute_factorial(i) /(compute_factorial(j)*compute_factorial(i-j));
    cout<<"\t"<<p;  
    
 
    }
   // cout<<"\t1";
    cout<<"\n";
    
  }
  
  
 return 0; 
}
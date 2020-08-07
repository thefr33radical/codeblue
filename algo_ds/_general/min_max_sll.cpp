#include<iostream>
#include<list>
using namespace std;

list<int> sort_order(list<int> &x)
{
  x.sort();
  
  return x;
  
  
}


list<int> min_max(list<int> &x)
{
 list<int>:: iterator i;
 
 int j=1,half=(x.size())/2,temp;
 
  i=x.begin();
 while(j<half)
 {
   i++;
   temp=x.back();
    x.pop_back();
   
   x.insert(i,temp);
  
   
  j++; 
 }
 
 cout<<"\n"<<"popped elements\n\n";
 
  for(i=x.begin();i!=x.end();i++)
  {
    cout<<(*i)<<"\t";
    
  }
  
  return x;
  
}

int main()
{
  cout<<"\e[2J\e[H";
  list<int> l({1,35,45,87,98,4,5,5,48,8});
  
  list<int>::iterator i;
  l=sort_order(l);
  
  
    
  for(i=l.begin();i!=l.end();i++)
  {
    cout<<(*i)<<"\t";
    
  }
  
  l=min_max(l);
  
 return 0;
}
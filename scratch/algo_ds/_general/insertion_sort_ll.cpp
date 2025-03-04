#include<iostream>
#include<list>
using namespace std;

list<int> sort_order(list<int> &x)
{
  x.sort();
  
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
  
  
 return 0;
}
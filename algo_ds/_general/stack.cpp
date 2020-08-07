//linked list implementation

#include<iostream>
#include<stdlib.h>

using namespace std;

struct node
{
  int val;
  struct node *next;
  };


  
struct node* pushfront(struct node **head, int v)
{
  struct node *temp=new node;
if(!head)
{
*head=new node;
(*head)->next=NULL;
(*head)->val=v;

  return *head;
}  
temp->val=v;
temp->next=*head;
return temp;
}



void print(struct node **head)
{
  struct node* temp;
  
  temp=*head;
  cout<<"\n";
  while(temp)
  {
    cout<<"\t"<<temp->val;
    temp=temp->next;
    
  }
    
  return;
}

struct node* deletefront(struct node **head)
{
  
  if(!(*head))
  {
   cout<<"\n stack is empty";
   return *head;
  }
  
  struct node* temp;
  temp=*head;
  
  *head=(*head)->next;
  delete (temp);
  
  return *head;  
}



int main()
{
  cout<<"\e[1;1H\e[2J";
  //system("clear");
  int input,v;
  struct node *head;
    
  while(1)
  {
  cout<<"\n 1. Push elements to stack \n 2. Remove elements from the stack \n 3. Print stack \n 4.Exit";
  
  cin>>input;
  
  if(input==4)
    exit(0);
 
  if(input==1)
  {
    cin>>v;
    head=pushfront(&head,v);
  }
  
   if(input==2)
  {
    
    head=deletefront(&head);
  }
  
  if(input==3)
  {
    //cin>>v;
    print(&head);
  }
  
  
  }  
  return 1;
}



































































































































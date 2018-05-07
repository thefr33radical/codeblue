#include<iostream>
#include<stdlib.h>

using namespace std;

struct node
{
int val;
struct node* next;
struct node* prev;
};

typedef struct node* N;


void ins_front(N *header,int v)
{
    N temp=new node();
    N temp2=new node();

    if(!(*header))
    {
    *header=new node();
    (*header)->val=v;
    (*header)->next=*header;

    return;
    }
   else
   {
   temp=*header;
cout<<"\n ok";
         while((temp->next)!=*header)
        {
        temp=temp->next;
        }
cout<<"\n ok";
        temp2->val=v;
        temp2->next=*header;
        temp->next=temp2;
        *header=temp2;

    return;
    }
}

void ins_rear(N *header,int v)
{
    N temp=new node();
    N temp2=new node();

    if(!(*header))
    {
    *header=new node();
    (*header)->val=v;
     (*header)->next=*header;

    return;
    }

    else
    {
        temp=*header;
        while((temp->next)!=*header)
        {
        temp=temp->next;

        }
        temp2->val=v;
        temp2->next=*header;
        temp->next=temp2;
        return;
    }
}

void print(N *header)
{
int count=0;
N temp=new node();
temp=*header;
if(temp)
{
do
{
count++;
std::cout<<"\n"<<temp->val;
cout<<"\n Th count value is"<<count;
temp=temp->next;
}while(temp->next!=*header);
std::cout<<"\n"<<temp->val;
}
}

int main()
{

N head;
int i=0,input,v;

cout<<"\n Enter the options: ";

while(true)
{
cout<<"\n 1. Insert @ rear\n 2. Insert @ front \n 7.Exit\n";
cin>>input;

if(input==1)
{
cout<<"Enter the node to insert";
cin>>v;
ins_rear(&head,v);
print(&head);
}

if(input==2)
{
cout<<"Enter the node to insert";
cin>>v;
ins_front(&head,v);
print(&head);
}


if(input==7)
{
exit(0);
}

}
return 0;

}

#include<iostream>

using namespace std;


struct node
{
    int val;
    node *next;

};

struct node* insertfront(int v,struct node* head)
{
    struct node *temp=new node;
    temp->val=v;
    temp->next=head;
    return temp;

}

int main()
{


int i=0,count=0;
    node *head=new node;
    node *temp=new node;
    node *store=new node;
    node *slowptr=new node;
    node *fastptr= new node;




    while(i<10)
    {
    head=insertfront(i,head);
    i++;
    }


    temp=head;

    while(temp)
    {
        //cout<<temp->val;
        count++;
        if(count==2)
        store=temp;
        temp=temp->next;

    }

     temp=head;
      while(temp->next)
    {
        cout<<temp->val<<"\t";
        temp=temp->next;


    }
    temp->next=store; //loop formed

    slowptr=head;
    fastptr=head;

    while(slowptr&&fastptr)
    {


        fastptr=fastptr->next;

        if(fastptr==(slowptr))
        {
            cout<<"\n floyd cycle exists";
            return 1;
        }
         fastptr=fastptr->next;

         if(fastptr==NULL)
         {  cout<<"\n floyd cycle dosen't exist";
         return 0;
         }

          if(fastptr==(slowptr))
        {
            cout<<"\n floyd cycle exists";
            return 1;
        }

        slowptr=slowptr->next;

    }




     cout<<"\n floyd cycle dosen't exists";

     return 0;
}

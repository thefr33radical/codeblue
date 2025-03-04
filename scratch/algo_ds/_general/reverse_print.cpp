#include<iostream>

using namespace std;


struct node
{
    int val;
    node *next;

};

struct node* insertfront(int v,struct node** head)
{
    struct node *temp=new node;
    temp->val=v;
    temp->next=*head;
    return temp;

}

void ReversePrint(struct node** head)
{
  // This is a "method-only" submission.
  // You only need to complete this method.


    node *temp=new node();
    node *temp2=new node();
    int c=0;
     temp=*head;

    if(!(*head))
        return;

    temp=*head;

    while(temp)
        {
        cout<<temp->val<<"\n";
        temp=temp->next;

        c++;
        cout<<"count value:"<<c;
    }

temp=*head;
temp2=temp;
    while(c)
        {
        if(c>1)
            {

            while(temp->next)
                {
                temp2=temp;
                temp=temp->next;
            }


            cout<<temp->val;
            temp2->next=NULL;
            //delete temp;
            temp=temp2;
            c--;
        }
        else
            {
             cout<<temp->val;
             //delete temp;

            return;
        }
    }
}

int main()
{
    struct node *head,*te;
    te= new node;
    head=new node;
    head->next=NULL;

    int n,t,i=1;

std::cout<<"Enter the number of nodes to insert :";
cin>>n;
while(i<=n)
{
    cout<<"\n Enter next number";
    cin>>t;
           insertfront(t,&head);

        i++;
}
ReversePrint(&head);

te=head;

while(te)
{
        cout<<"\n"<<te->val<<"\t these are te values\n";
    te=te->next;
}
    return 0;
}

#include<iostream>

using namespace std;



int leftr[5],rightr[5];
int i,j;

struct node
{
int val;
node *left;
node *right;
};

node* newnode(int v)
{
node *temp=new node;
temp->left=NULL;
temp->right=NULL;
temp->val=v;

return temp;
}

void traverse_left(node *temp)
{

if(temp==NULL)
return;

leftr[i]=temp->val;
i=i+1;
cout<<temp->val<<"\t"<<"\n";
traverse_left(temp->left);

}

void traverse_right(node *temp)
{
if(temp==NULL)
return;

rightr[j]=temp->val;
j=j+1;
cout<<temp->val<<"\n";
traverse_right(temp->right);

return;
}


int main()
{
node *head=newnode(1);
head->left=newnode(2);
head->right=newnode(3);
head->left->left=newnode(4);
head->left->right=newnode(5);
head->right->left=newnode(6);
head->right->right=newnode(7);
head->right->right->right=newnode(9);
head->left->left->left=newnode(8);

traverse_left(head);
traverse_right(head);

cout<<"----------------------------";
for(i=0;i<5;i++)
{
if(i%2==0)
cout<<"\n"<<leftr[i]<<"\t"<<rightr[i+1];

}

return 0;

}


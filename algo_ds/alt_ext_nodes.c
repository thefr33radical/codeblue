#include<stdio.h>



struct NODE
{

NODE *left;
NODE *right;
int val;

};
typedef struct NODE node;

int left[10];
int right[10];
int i;


int traverse_left(node *temp)
{

if(temp->left==NULL)
return;

left[i]=temp->val;
i++;
traverse(temp->left);

}


int traverse_right(node *temp)
{
if(temp->right==NULL)
return;

right[i]=temp->val;
i++;
traverse(temp->right);

}



int main()
{

left (&head);
i=0;
right(&head);



return 0;
}

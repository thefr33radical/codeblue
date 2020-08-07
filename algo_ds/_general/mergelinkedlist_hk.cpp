/*
  Merge two sorted lists A and B as one linked list
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* MergeLists(Node *headA, Node* headB)
{
  // This is a "method-only" submission. 
  // You only need to complete this method 
    
    struct Node *temp1=new Node;
    struct Node *temp2=new Node;
    struct Node *temp3=new Node;
    struct Node *headC=new Node;
    struct Node *temp4=new Node;
    
    if(!(headA)&&!(headB))
        {
            return NULL;      
        }
    
    if(!(headA))
        return headB;
    
     
    if(!(headB))
        return headA;
    
   temp1=headA;
    temp2=headB;
    temp3=headC;
    
    while(temp1||temp2)
	  {
	      
            
                temp3=headC;
                if(!temp1)
                 {
                    while(temp3->next)
                        {
                        temp3=temp3->next;
                        
                        }
                    
                    temp4=new Node;
                    temp4->data=temp2->data;
                    temp4->next=NULL;
                    
                    temp3->next=temp4;
                    temp2=temp2->next;
                    //cout<<temp3->data;
                    continue;
                }
        
        
        
                 if(!temp2)
                    {
                    while(temp3->next)
                        {
                        temp3=temp3->next;
                        
                        }
                    temp4=new Node;
                    temp4->data=temp1->data;
                    temp4->next=NULL;
         
                    temp3->next=temp4;
                    temp1=temp1->next;
                    continue;
                }
        
        
         temp3=headC;
          if((temp1->data)<=(temp2->data))
                    {
                   
                     while(temp3->next)
                        {
                        temp3=temp3->next;
                        
                        }
                    temp4=new Node;
                    temp4->data=temp1->data;
              
                    temp4->next=NULL;
                    
                    temp3->next=temp4;
                    temp1=temp1->next;
                }
        
                else
                    { 
                    
                    while(temp3->next)
                        {
                        temp3=temp3->next;
                       
                           }
                    
                    temp4=new Node;
                    temp4->data=temp2->data;
                    temp4->next=NULL;
                    
                    temp3->next=temp4;
                    temp2=temp2->next;
                    
                     }
                
                
        
        
        
    }
        
    
    return headC;
    
}

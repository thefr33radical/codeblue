'''
Given a snake & ladder board with only ladders and no snakes, find the minimum times one has to roll dice to reach the destination.
Follow up question – include snakes on the board and find the same.

'''

#T(C)=O(N) where n is the number of squares in snake and ladder
from collections import deque
class node:
    def __init__(self):
        self.v=0
        self.dist=0
        
def find_min_path(mat):
    visited=[False for i in range(len(mat)) ]
    #print(visited,mat)
    
        
    q=deque()
    initial=node()
    initial.v=0
    initial.dist=0
    q.append(initial)
    #print(q)
    visited[0]=True
    #print(mat,visited)
    while(q):
        temp=q.popleft()
        v=temp.v
        print(temp.dist,temp.v)
        # print(v,dist)
       
        if(v==  len(mat)):
            break
        
        i=v+1
        while i<=v+6 and i <=len(mat):
            if(visited[i]==False):
                
                temp2=node()
                temp2.dist=temp.dist+1
                visited[i]=True
                
                if(mat[i]!=-1):
                    temp2.v=mat[i]
                else:
                    temp2.v=i
                q.append(temp2)
            i+=1
                
    
    '''
    N=len(mat)
   # The graph has N vertices. Mark all
    # the vertices as not visited
    visited = [False] * N
 
    # Create a queue for BFS
    queue = deque()
 
    # Mark the node 0 as visited and enqueue it
    visited[0] = True
    temp=node()
    temp.v=0
    temp.dist=0
    # Distance of 0't vertex is also 0
    # Enqueue 0'th vertex
    queue.append(temp)
 
    # Do a BFS starting from vertex at index 0
    qe = node() # A queue entry (qe)
    while queue:
        qe = queue.popleft()
        v = qe.v # Vertex no. of queue entry
 
        # If front vertex is the destination
        # vertex, we are done
        if v == N - 1:
            break
 
        # Otherwise dequeue the front vertex 
        # and enqueue its adjacent vertices 
        # (or cell numbers reachable through
        # a dice throw)
        j = v + 1
        while j <= v + 6 and j < N:
         
            # If this cell is already visited,
            # then ignore
            if visited[j] is False:
                 
                # Otherwise calculate its 
                # distance and mark it 
                # as visited
                a = node()
                a.dist = qe.dist + 1
                visited[j] = True
 
                # Check if there a snake or ladder
                # at 'j' then tail of snake or top
                # of ladder become the adjacent of 'i'
                a.v = mat[j] if mat[j] != -1 else j
 
                queue.append(a)
 
            j += 1
 
    # We reach here when 'qe' has last vertex
    # rrhe distance of vertex in 'qe
    print(qe.dist)
    '''

def compute():
    moves=[]
    N = 30
    for i in range(1,N+1):
        moves.append(-1)
 
    moves[2] = 21
    moves[4] = 7
    moves[10] = 25
    moves[19] = 28
 

    moves[26] = 0
    moves[20] = 8
    moves[16] = 3
    moves[18] = 6
    
   
    find_min_path(moves)
 

if __name__=="__main__":
    compute()

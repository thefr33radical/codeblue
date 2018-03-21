# Definition for an interval.
class Interval:
     def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval

    def sorter(self,interval):
       
        for i in range(len(interval)):
            for j in range(len(interval)):
                if(interval[i].start<interval[j].start):
                   
                    temp1=interval[i].start
                    temp2=interval[i].end
                    
                    interval[i].start=interval[j].start
                    interval[i].end=interval[j].end
                    
                    interval[j].start=temp1
                    interval[j].end=temp2
                    
        return interval

    def insert(self, intervals):
        
       pass
        
if __name__=="__main__":
    l=[[1,17],[8,10],[3,5],[12,16],[30,31],[6,9],[7,19],[39,45]] 
    new_l=[]
    for i in range(len(l)):
        j=Interval()
        j.start=l[i][0]
        j.end=l[i][1]
        #print (l[i][0])
        new_l.append(j)
        
     
    
    s=Solution()
  
    

    print("\nInput:")
    for i in new_l:
        print(i.start,i.end)  
        
    new_l=s.sorter(new_l)
    
    print("\nSorted:")
    for i in new_l:
        print(i.start,i.end) 
    
    newer_l=s.insert(new_l)
        
    print("\nOutput : ")
    for i in newer_l:
        print(i.start,i.end)
        
        
   
        
        
      
    
    
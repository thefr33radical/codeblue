
#Problem : Merge intervals that overlap each other
#T(C)=O(n) for a sorted list of intervals, O(nlogn) for unsorted list of intervals
# Definition for an interval.
class Interval:
     def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
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
    #function to merge list which overlap each other
    def insert(self, intervals):
        l=[]
        i=1
        sz=len(intervals)
        obj=Interval()
        obj.start=intervals[0].start
        obj.end=intervals[0].end
        j=0
        l.append(obj)
       # print ("condition2")
        while i<sz:
            #for x in l:
                #print(x.start,x.end)    
            #Overlap Condition
            if (intervals[i].start<l[j].end):
                #obj interval end >  current interval end
                if(intervals[i].end<l[j].end):
                        #print ("condition2 intervals[i].end<l[j].end",intervals[i].start,l[j].end)
                    i+=1
                    continue
                #obj interval  end is less than current interval end
                elif(intervals[i].end>l[j].end):
                    l[j].end=intervals[i].end
                        #print ("condition3 intervals[i].end>l[j].end",intervals[i].end,l[j].end)
                    i+=1
                    continue
            else:
                #Dont Overlap Condition
                obj2=Interval()
                obj2.start=intervals[i].start
                obj2.end=intervals[i].end
                l.append(obj2)
                j+=1
                i+=1
                print ("condition4")
                #l.append(obj)
          
        return l
        
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
        
        
   
        
        
      
    
    
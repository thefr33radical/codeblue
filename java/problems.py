
# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dct={}
        
        start=0
        window=0
        
        for i in range(len(s)):
            # if letter is already seen
            if s[i] in dct:
                # choose the next letter of the prev(repeated charecter) as start
                start=max(start,dct[s[i]]+1)
                
            # Find the max window
            window=max(window,(i-start)+1)
            #update the current letter
            dct[s[i]]=i
    
        return window
    
    #4. Median of Two Sorted Arrays
    class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        temp=[]
        i=0
        j=0
        
        # Use merge Sort
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                temp.append(nums1[i])
                i+=1
            else:
                temp.append(nums2[j])
                j+=1
        while i<len(nums1):
            temp.append(nums1[i])
            i+=1
        while j<len(nums2):
            temp.append(nums2[j])
            j+=1
        l=len(temp)
        if l%2==0:
            return ((temp[int(l/2)-1]+temp[int(l/2)])/2)
        else:
            return temp[int(l/2)]
    
            
    
    

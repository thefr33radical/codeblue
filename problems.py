
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
    
    

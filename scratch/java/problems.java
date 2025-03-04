// https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/

import java.util.*;
class Solution {
    public int lengthOfLongestSubstring(String s) {
        
        Map<Character,Integer> m=new HashMap<> ();
        int start=0;
        int window=0;
        
         for(int i=0; i<s.length();i++)
        {   
             char k =s.charAt(i);
            if(m.containsKey(k))
               {    start=Math.max(m.get(k)+1,start);
                    }           
             window=Math.max(window,(i-start)+1);
             m.put(k,i);
                                  
        }
            
        return window;
    }
}

# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 23:17:49 2020

@author: Alex

code for windows
"""

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lengh = len(s)
        count = 0
        if lengh < 3:
            return 0
        for i in range(lengh-2):
            List = ['a', 'b', 'c']
            List.remove(s[i])       
            for j in range(i+1,lengh):
                if s[j] in List:
                    List.remove(s[j])
                if not List:
                    break
            if not List:
                #print(i,j,s[i:j+1])
                count += lengh - j
        return count
    
if __name__ == "__main__":
    s = Solution()
    a1 = "ababbbc"
    #a2 = 
    print(s.numberOfSubstrings(a1))
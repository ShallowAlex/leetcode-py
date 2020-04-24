# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 10:49:16 2020
@author: Alex
code for windows
"""
#from typing import List
class Solution:
    def numSteps(self, s: str) -> int:
        p = int(s, 2)
        ans = 0
        while p != 1:
            if p & 1 == 1:
                p += 1
            else:
                p >>= 1
            ans += 1
        return ans
                
if __name__ == "__main__":
    s = Solution()
    a1 = "1101"
    #a2 = 
    print(s.numSteps(a1))
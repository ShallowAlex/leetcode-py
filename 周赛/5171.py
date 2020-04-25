# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 11:39:50 2020

@author: Alex

code for windows
"""

class Solution:
    def closestDivisors(self, num):
        n = int((num+2)**0.5)
        for i in range(n+1)[::-1]:
            if (num+1) % i == 0:
                return [int((num+1)/i), i]
            elif (num+2) % i == 0:
                return [int((num+2)/i), i]

        
if __name__ == "__main__":
    s = Solution()
    a1 = 8
    #a2 = 
    print(s.closestDivisors(a1))
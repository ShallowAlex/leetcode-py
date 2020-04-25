# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 23:17:49 2020

@author: Alex

code for windows
"""

class Solution:
    def countOrders(self, n: int) -> int:
        def backtrack(n):
            if n == 1:
                return 1
            count1 = backtrack(n-1)
            n1 = 2*(n-1)+1
            count = (1+n1)*n1*count1/2
            return count % (10**9 + 7)
        return int(backtrack(n))
    
if __name__ == "__main__":
    s = Solution()
    a1 = 2
    #a2 = 
    print(s.countOrders(a1))
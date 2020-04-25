# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 16:38:56 2020

@author: Alex

code for windows
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        div = 0
        flag1 = flag2 = 1
        if dividend < 0:
            dividend = -dividend
            flag1 = -1
        if divisor < 0:
            divisor = -divisor
            flag2 = -1
        while dividend > divisor:
            n = 0
            while dividend > (divisor<<(n+1)):
                n += 1
            div += 1<<n
            dividend -= divisor<<n
        return div
    
if __name__ == "__main__":
    s = Solution()
    print(s.divide(10,3))
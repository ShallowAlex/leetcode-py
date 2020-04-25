# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 16:08:05 2020

@author: Alex

code for windows
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def add(tmp, l, r):
            if l == 0 and r == 0:
                reslut.append(tmp)
            if l > 0:
                add(tmp+'(', l-1, r)
            if r > l:
                add(tmp+')', l, r-1) 
        tmp = ''
        reslut = []
        left = right = n
        if n > 0:
            add(tmp, left, right)
        return reslut
    
if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(2))
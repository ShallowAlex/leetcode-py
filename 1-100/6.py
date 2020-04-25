# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 19:52:07 2020

@author: Alex

code for windows
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= 2 or numRows == 1:
            return s
        rows = ['' for i in range(min(len(s),numRows))] 
        flag = -1
        num = 0

        for letter in s:
            rows[num] += letter
            if num == 0 or num == numRows-1:
                flag *= -1
            num += flag
        
        return ''.join(rows)
    
s = Solution()
print(s.convert("PAYPALISHIRING",3))
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 20:27:06 2020

@author: Alex

code for windows
"""

class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []
        ans = [[1]]
        for i in range(1, numRows):
            lengh = len(ans[i-1]) + 1
            tmp = [1] * lengh
            for j in range(1, lengh-1):
                tmp[j] = ans[i-1][j-1] + ans[i-1][j]
            ans.append(tmp)
        return ans
        
if __name__ == "__main__":
    s = Solution()
    a1 = 5
    #a2 = 
    print(s.generate(a1))
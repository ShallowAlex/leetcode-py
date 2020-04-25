# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:11:10 2020

@author: Alex

code for windows
"""

class Solution:
    def spiralOrder(self, matrix):
        top = left = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1
        num = 0
        total = (bottom+1) * (right+1)
        ans = []
        while num < total:
            for i in range(left, right+1):
                ans.append(matrix[top][i])
                num += 1
                print(1,num)
            top += 1
            for i in range(top, bottom+1):
                ans.append(matrix[i][right])
                num += 1
                print(2,num)
            right -= 1
            for i in range(right, left-1, -1):
                ans.append(matrix[bottom][i])
                num += 1
                print(3,num)
            bottom -= 1
            for i in range(bottom, top-1, -1):
                ans.append(matrix[i][left])
                num += 1
                print(4,num)
            left += 1
        return ans

if __name__ == "__main__":
    s = Solution()
    a1 = [[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12]]
    #a2 = 
    print(s.spiralOrder(a1))
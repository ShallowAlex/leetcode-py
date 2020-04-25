# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 21:23:55 2020

@author: Alex

code for windows
"""

class Solution:
    def maxArea(self, height):
        i = 0
        j = len(height) - 1
        s = 0
        while i < j:
            tmp =min(height[i], height[j])
            s = max(s, (j-i)*tmp)
            if height[i] == tmp:
                while height[i] <= tmp and i < j:
                    i += 1
            else:
                while height[j] <= tmp and i < j:
                    j -= 1
        return s


s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
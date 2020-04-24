# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 14:25:10 2020

@author: Alex

code for windows
"""

class Solution:
    def longestCommonPrefix(self, strs):
        flag = True
        l = len(strs)
        nums = 0
        for nums in range(len(strs[0])):
            for i in range(l):
                if nums < len(strs[i]) and strs[i][nums] == strs[0][nums]:
                    continue
                else: 
                    flag = False
                    break
            if not flag:
                break
        return strs[0][:nums]
    
q = ["flower","flow","flight"]

s = Solution()
print(s.longestCommonPrefix(q))
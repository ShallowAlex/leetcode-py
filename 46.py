# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:31:04 2020

@author: Alex

code for windows
"""

class Solution:
    def permute(self, nums):
        def backtrack(nums1):
            if not nums1:
                result.append(tmp[:])
            for i in range(len(nums1)):
                tmp.append(nums1[i])
                backtrack(nums1[:i]+nums1[i+1:])
                tmp.pop()
        result = []
        if nums:
            for i in range(len(nums)):
                tmp = [nums[i]]
                backtrack(nums[:i]+nums[i+1:])
        return result

if __name__ == "__main__":
    s = Solution()
    arr = [1,2,3]
    print(s.permute(arr))
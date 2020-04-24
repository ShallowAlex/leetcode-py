# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 14:58:55 2020

@author: Alex

code for windows
"""

class Solution:
    def threeSum(self, nums):
        tmp = []
        if len(nums) < 3:
            return tmp
        nums.sort()
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while left < right:
                sum1 = nums[i]+nums[left]+nums[right]
                if sum1 > 0:
                    right -= 1
                elif sum1 < 0:
                    left += 1
                else:
                    tmp.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        return tmp


a = [-2,0,0,2,2]
s = Solution()
print(s.threeSum(a))
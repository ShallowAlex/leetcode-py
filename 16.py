# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 16:59:34 2020

@author: Alex

code for windows
"""

class Solution:
    def threeSumClosest(self, nums, target):
        def gapcal(arr):
            i, j, k = arr
            return target-i-j-k
        if len(nums) < 3:
            return []
        nums.sort()
        tmp = nums[:3]
        gap = gapcal(tmp)
        for i in range(len(nums)-2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                tmp1 = [nums[i], nums[left], nums[right]]
                gap1 = gapcal(tmp1)
                if abs(gap) > abs(gapcal(tmp1)):
                    tmp = tmp1
                    gap = gap1
                if gap1 > 0:
                    left += 1
                elif gap1 < 0:
                    right -= 1
                else:
                    return target
        return sum(tmp)

if __name__ == "__main__":
    s = Solution()
    arr = [1,2,4,8,16,32,64,128]
    print(s.threeSumClosest(arr,82))
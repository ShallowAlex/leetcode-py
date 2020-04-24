# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 14:17:28 2020

@author: Alex

code for windows
"""

class Solution:
    def fourSum(self, nums, target):
        #双指针i,j定，left,right动
        nums.sort()
        n = len(nums)
        if n < 4:
            return []
        reslut = []
        for i in range(n-3):
            if nums[i] + nums[i+1]*3 > target:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,n-2):
                if nums[i] + nums[j] + nums[j+1]*2 > target:
                    break
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                left = j + 1
                right = n - 1
                while left < right:
                    gap =target - (nums[i] + nums[j] + nums[left] + nums[right])
                    if gap > 0:
                        left += 1
                    elif gap < 0:
                        right -= 1
                    else:
                        reslut.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
        return reslut

if __name__ == "__main__":
    s = Solution()
    arr = [1,0,-1,0,-2,2]
    print(s.fourSum(arr,0))

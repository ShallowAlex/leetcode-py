# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 11:02:32 2020

@author: Alex

code for windows
"""
class Solution:
    def searchRange(self, nums, target):
        left = 0
        right = len(nums) - 1
        mid1 = mid2 = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                l1 = left
                r1 = mid
                l2 = mid
                r2 = right
                mid1 = (l1 + r1) // 2
                mid2 = (l2 + r2 + 1) // 2
                while l1 < r1:
                    if nums[mid1] < target:
                        l1 = mid1 + 1
                    else:
                        r1 = mid1
                    mid1 = (l1 + r1) // 2
                while l2 < r2:
                    if nums[mid2] > target:
                        r2 = mid2 - 1
                    else:
                        l2 = mid2
                    mid2 = (l2 + r2 + 1) // 2
                break
        return [mid1,mid2]


if __name__ == "__main__":
    s = Solution()
    nums = [5,7,7,8,8,10]
    print(s.searchRange(nums,10))
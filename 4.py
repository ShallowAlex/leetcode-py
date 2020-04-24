# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 17:26:35 2020

@author: Alex

code for windows
"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 > len2:
            len1, len2 = len2, len1
            nums1, nums2 = nums2, nums1
        left = 0
        right = len1
        half_len = (len1 + len2 + 1) // 2
        while left <= right:
            mid1 = (left + right) // 2
            mid2 = half_len - mid1
            if mid1 < len1 and nums2[mid2-1] > nums1[mid1]:
                left = mid1 + 1
            elif mid1 > 0 and nums1[mid1-1] > nums2[mid2]:
                right = mid1 - 1
            else:
                if mid1 == 0:
                    maxleft = nums2[mid2-1]
                elif mid2 == 0:
                    maxleft = nums1[mid1-1]
                else:
                    maxleft = max(nums1[mid1-1], nums2[mid2-1]) 

                if (len1+len2)%2 == 1:
                    return maxleft
                if mid1 == len1:
                    minright = nums2[mid2]
                elif mid2 == len2:
                    minright = nums1[mid1]
                else:
                    minright = min(nums1[mid1], nums2[mid2])
                return (maxleft+minright) / 2.0

s = Solution()
print(s.findMedianSortedArrays([1,3],[2]))
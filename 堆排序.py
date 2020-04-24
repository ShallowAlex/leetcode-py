# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 14:09:44 2020
@author: Alex
code for windows
"""
from typing import List
class Solution:
    def HeapSort(self, nums):
        #build heap
        for i in range(len(nums)//2, -1, -1):
            self.heapify(nums, i, len(nums))
        #将最大放到最后,对前面的求最大
        for i in range(len(nums)-1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.heapify(nums, 0, i)

    def heapify(self, nums, root, heap_len):
        p = root
        while p * 2 + 1 < heap_len:
            left, right = p * 2 + 1, p * 2 + 2
            if heap_len <= right or nums[right] < nums[left]:
                large = left
            else:
                large = right
            if nums[p] < nums[large]:
                nums[p], nums[large] = nums[large], nums[p]
                p = large
            else:
                break

    def sortArray(self, nums: List[int]) -> List[int]:
        self.HeapSort(nums)
        return nums

if __name__ == "__main__":
    s = Solution()
    a1 = [ 12, 11, 13, 5, 6, 7] 
    #a2 = 
    print(s.sortArray(a1))
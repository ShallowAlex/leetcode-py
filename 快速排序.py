# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 11:24:44 2020
@author: Alex
code for windows
"""
#from typing import List
class Solution:
    def random_partition(self, arr, left, right):
        import random
        pivot = random.randint(left, right)
        arr[right], arr[pivot] = arr[pivot], arr[right]
        index = left
        for i in range(left, right):
            if arr[i] < arr[right]:    
                arr[i], arr[index] = arr[index], arr[i]
                index += 1
        arr[index], arr[right] = arr[right], arr[index]
        return index

    def QuickSort(self, arr, left=0, right=None):
        if right <= left:
            return
        mid = self.random_partition(arr, left, right)
        self.QuickSort(arr, left, mid-1)
        self.QuickSort(arr, mid+1, right)

    def sortArray(self, arr):
        self.QuickSort(arr, 0, len(arr)-1)
        return arr
    
    

if __name__ == "__main__":
    s = Solution()
    a1 = [7,5,3,7,9,4,3]
    #a2 = 
    print(s.sortArray(a1))
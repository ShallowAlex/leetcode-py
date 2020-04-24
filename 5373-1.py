# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 22:51:53 2020
@author: Alex
code for windows
"""
#from typing import List
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        tmp = [1, 1]
        while tmp[-1] <= k:
            tmp.append(tmp[-1]+tmp[-2])
        tmp = tmp[1:-1]
        #print(tmp)
        i = len(tmp) - 1
        cnt = 0
        while k != 0:
            if tmp[i] > k:
                i -= 1
            else:
                k -= tmp[i]
                cnt += 1
        return cnt

if __name__ == "__main__":
    s = Solution()
    a1 = 513314
    #a2 = 
    print(s.findMinFibonacciNumbers(a1))
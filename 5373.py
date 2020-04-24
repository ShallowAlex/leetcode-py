# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 22:18:23 2020
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
        tmp = tmp[::-1]
        print(tmp)
        def helper(k, tmp):
            if k in tmp:
                return 1
            cnt = k
            for i in tmp:
                if i > k:
                    continue
                cnt = min(cnt, helper(k-i, tmp)+1)
            return cnt
        return helper(k, tmp)



if __name__ == "__main__":
    s = Solution()
    a1 = 513314
    #a2 = 
    print(s.findMinFibonacciNumbers(a1))
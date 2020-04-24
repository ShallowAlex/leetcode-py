# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 10:25:46 2020

@author: Alex

code for windows
"""
from typing import List
import functools
class Solution:
    def sumFourDivisors(self, nums):
        @functools.lru_cache(maxsize=None)
        def cal(number):
            if number == 1:
                return {1}
            s = set([1, number])
            for i in range(2,int(number//2)):
                if number % i == 0:
                    s.add(i)
                    s.update(cal(int(number/i)))
                    if len(s) > 4:
                        return s
            return s
        count = 0
        for i in nums:
            tmp = cal(i)
            print(tmp)
            if len(tmp) == 4:
                count += sum(tmp)
        return count
    
if __name__ == "__main__":
    s = Solution()
    a1 = [21,4,7]
    #a2 = 
    print(s.sumFourDivisors(a1))

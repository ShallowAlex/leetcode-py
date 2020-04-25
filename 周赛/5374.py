# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 23:14:58 2020
@author: Alex
code for windows
"""
#from typing import List
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 * (2**(n-1)):
            return ''
        ans = ''
        stack = ['a','b','c']
        k -= 1
        while n > 0:
            tmp = stack[k // 2**(n-1)]
            ans += tmp
            stack = ['a','b','c']
            stack.remove(tmp)
            k = k % (2**(n-1))
            n -= 1
        return ans

if __name__ == "__main__":
    s = Solution()
    #a1 = 
    #a2 = 
    print(s.getHappyString(10,100))
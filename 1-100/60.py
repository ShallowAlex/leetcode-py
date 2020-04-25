# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 17:34:24 2020

@author: Alex

code for windows
"""

class Solution:
    def getPermutation(self, n, k):
        import math
        tmp = ''
        q = math.factorial(n-1)
        k -= 1
        arr = [i for i in range(1, n+1)]
        while arr:
            num = int(k // q)
            k = k % q
            n -= 1
            if n == 0:
                n += 1
            q = q // n
            tmp += str(arr[num])
            arr.pop(num)
        return  tmp

if __name__ == "__main__":
    s = Solution()
    a1 = 3
    a2 = 3
    print(s.getPermutation(a1, a2))
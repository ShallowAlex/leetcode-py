# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 22:10:26 2020
@author: Alex
code for windows
"""
#from typing import List
class Solution:
    def countLargestGroup(self, n: int) -> int:
        tmp = [[]]
        for i in range(1,n+1):
            b = 0
            tmp_n = i
            while tmp_n:
                b += tmp_n%10
                tmp_n //= 10
            if len(tmp) <= b:
                tmp.append([i])
            else:
                tmp[b].append(i)
        j = map(len, tmp)
        return list(j)


if __name__ == "__main__":
    s = Solution()
    a1 = 531
    #a2 = 
    print(s.countLargestGroup(a1))
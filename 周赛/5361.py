# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 00:09:55 2020
@author: Alex
code for windows
"""
#from typing import List
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        cntd = dict()
        for l in s:
            if l not in cntd:
                cntd[l] = 1
            else:
                cntd[l] += 1
        a = list(cntd.values())
        cntodd = 0
        prod = 1
        for i in a:
            if i % 2 == 1:
                cntodd += 1
        print(cntd, a)
        return cntodd <= k and len(s) >= k
    

if __name__ == "__main__":
    s = Solution()
    a1 = 'appllppaette'
    #a2 = 
    print(s.canConstruct(a1,2))
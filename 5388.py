# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 10:18:52 2020
@author: Alex
code for windows
"""
#from typing import List
class Solution:
    def reformat(self, s: str) -> str:
        tmp1 = list(s)
        tmp1.sort()
        tmp2 = []
        dic = set([str(i) for i in range(10)])
        while tmp1 and tmp1[-1] not in dic:
            tmp2.append(tmp1.pop())
        if abs(len(tmp1)-len(tmp2)) > 1:
            return ''
        if len(tmp1) < len(tmp2):
            tmp1, tmp2 = tmp2, tmp1
        ans = ''
        for i in range(len(tmp2)):
            ans += tmp1.pop() + tmp2.pop()
        if tmp1:
            ans += tmp1[0]
        return ans


if __name__ == "__main__":
    s = Solution()
    a1 = "ab1234"
    #a2 = 
    print(s.reformat(a1))
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 21:08:22 2020

@author: Alex

code for windows
"""

class Solution:
    def reverse(self, x: int) -> int:
        flag = 1
        if x < 0:
            flag = -1
            x = abs(x)
        y = 0
        maxint = 2**31-1 #减1后没有退位情况，正负不分开讨论了

        while x != 0:
            if y > maxint//10:
                return 0
            tmp = x % 10
            y = y * 10 + tmp
            x = x//10

        if x > 2**30 - 1:
            if flag == 1:
                if tmp > maxint%10:
                    return 0
            else:
                if tmp > (maxint+1)%10:
                    return 0

        return y*flag
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 15:54:31 2020

@author: Alex

code for windows
"""

class Solution:
    def longestPalindrome(self, s):
        lengh = len(s)
        if lengh < 2:
            return s
        longest = 0

        def max_on_point(s,left,right):
            while left >= 0 and right < lengh and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - left - 1

        for i in range(lengh):
            l_odd, long_odd = max_on_point(s, i, i)
            l_even, long_even = max_on_point(s, i, i+1)
            if long_odd > longest or long_even > longest:
                left = min(l_odd, l_even)
                longest = max(long_odd, long_even)
            if i+longest//2 > lengh-1:
                break
        return s[left:left+longest]
        
s = Solution()
print(s.longestPalindrome("babad"))
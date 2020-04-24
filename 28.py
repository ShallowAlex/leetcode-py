# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 14:42:48 2020

@author: Alex

code for windows
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        pre = 0
        n = len(needle)
        if not needle:
            return 0
        while pre+n <= len(haystack):
            for i in range(n):
                if haystack[pre+i] != needle[i]:
                    j = n - 1
                    while j > 0 and pre+n < len(haystack):
                        if needle[j] == haystack[pre+n]:
                            break
                        j -= 1
                    pre = pre+ n - j
                    break
                elif i == n-1:
                    return pre
        return -1
    
if __name__ == "__main__":
    s = Solution()
    a = 'aaaaa'
    b = 'bba'
    print(s.strStr(a,b))
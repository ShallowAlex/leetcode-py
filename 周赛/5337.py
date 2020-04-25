# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 00:11:45 2020

@author: Alex

code for windows
"""

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        index = {(0, 0, 0, 0, 0): -1}
        cnt = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        ans = 0
        for i, c in enumerate(s):
            if c in 'aeiou':
                cnt[c] += 1
                cnt[c] %= 2
            key = tuple(cnt.values())
            if key not in index:
                index[key] = i
            else:
                ans = max(ans, i - index[key])
        return ans
    
if __name__ == "__main__":
    s = Solution()
    a1 = "elele"
    #a2 = 
    print(s.findTheLongestSubstring(a1))
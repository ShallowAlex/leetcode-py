# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 22:04:20 2020

@author: Alex

code for windows
"""
import collections
class Solution:
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)-ord('a')] += 1
            ans[tuple(count)].append(s)
        print(ans.values)
        return list(ans.values())
    
if __name__ == "__main__":
    s = Solution()
    a1 = ["eat","tea","tan","ate","nat","bat"]
    #a2 = 
    print(s.groupAnagrams(a1))
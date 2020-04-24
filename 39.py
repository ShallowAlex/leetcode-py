# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 20:04:03 2020

@author: Alex

code for windows
"""

class Solution:
    def combinationSum(self, candidates, target):
        def dfs(tmp, newtarget, index):
            if newtarget == 0:
                result.append(tmp[:])
                
            for i in candidates[index:]:
                new_target = newtarget - i
                if new_target < 0:
                    break
                tmp.append(i)
                dfs(tmp, new_target, candidates.index(i))
                tmp.pop()
        lengh = len(candidates)
        if lengh == 0:
            return []
        candidates.sort()
        result = []
        dfs([], target, 0)
        return result

if __name__ == "__main__":
    s = Solution()
    arr = [1,1,2,2,2,2]
    print(s.combinationSum([2,3,5],8))
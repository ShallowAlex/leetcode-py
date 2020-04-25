# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 20:04:03 2020

@author: Alex

code for windows
"""

class Solution:
    def combinationSum2(self, candidates, target):
        def dfs(tmp, newtarget, index, end):
            if newtarget == 0:
                result.append(tmp[:])
                
            for i in range(index, end):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                new_target = newtarget - candidates[i]
                if new_target < 0:
                    break
                tmp.append(candidates[i])
                dfs(tmp, new_target, i+1, end)
                tmp.pop()
        lengh = len(candidates)
        if lengh == 0:
            return []
        candidates.sort()
        result = []
        dfs([], target, 0, lengh)
        return result

if __name__ == "__main__":
    s = Solution()
    arr = [1,1,1,1,2,2,2]
    print(s.combinationSum([1,1,1,1,2,2,2,2],8))
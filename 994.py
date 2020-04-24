# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 14:37:20 2020

@author: Alex

code for windows
"""
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        pre = []
        cur = []
        ans = 0
        count = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    pre.append((i, j))
                elif grid[i][j] == 1:
                    count += 1
        if count == 0:
            return ans
        while pre:
            pre_i, pre_j = pre.pop()
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                cur_i, cur_j = pre_i + di, pre_j + dj
                if cur_i >= 0 and cur_j >= 0 and cur_i < m and cur_j < n and grid[cur_i][cur_j] == 1:
                    grid[cur_i][cur_j] = 2
                    count -= 1
                    cur.append((cur_i, cur_j))
            if not pre:
                pre = cur
                cur = []
                ans += 1
        return ans - 1 if count == 0 else -1
    
if __name__ == "__main__":
    s = Solution()
    a1 = [[2,1,1],[1,1,0],[0,1,1]]
    #a2 = 
    print(s.orangesRotting(a1))
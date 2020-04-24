# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 11:40:20 2020
@author: Alex
code for windows
"""
from typing import List
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        m = len(board)
        n = len(board[0])
        ans = 0
        flag = 0
        for x in range(m):
            for y in range(n):
                if board[x][y] == 'R':
                    flag = 1
                    break
            if flag:
                break
        d = [[0,1], [0,-1], [1,0], [-1,0]]
        for dx, dy in d:
            cur_x = x + dx
            cur_y = y + dy
            while cur_x >= 0 and cur_x < m and cur_y < n and cur_y >= 0:
                #print(cur_x, cur_y)
                if board[cur_x][cur_y] == 'p':
                    ans += 1
                    break
                elif board[cur_x][cur_y] == 'B':
                    break
                cur_x += dx
                cur_y += dy
        return ans

if __name__ == "__main__":
    s = Solution()
    a1 = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
    #a2 = 
    print(s.numRookCaptures(a1))
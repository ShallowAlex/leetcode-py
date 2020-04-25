# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 12:00:10 2020
@author: Alex
code for windows
"""
#from typing import List
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        if k == 0 or m <= k-1:
            return 0
        dp = [[[0]*(k+1) for j in range(m+1)] for i in range(n+1)]
        for i in range(1, m+1):
            dp[0][i][1] = 1
        for i in range(1, k+1):
            for j in range(1, m+1):
                for l in range(1, k+1):
                    for num in range(1, j):
                        dp[i][j][l] += dp[i-1][num][l]
                    for num in range(j, m+1):
                        dp[i][j][l] += dp[i-1][num][l-1]
                    if dp[i][j][l] > (10**9+7):
                        dp[i][j][l] %= (10**9+7)
        print(dp)
        return dp[-1][-1][-1]
    
if __name__ == "__main__":
    s = Solution()
    #a1 = 
    #a2 = 
    print(s.numOfArrays(2,3,1))
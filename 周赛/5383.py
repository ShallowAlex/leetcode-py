# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 11:43:22 2020
@author: Alex
code for windows
"""
#from typing import List
class Solution:
    def numOfWays(self, n: int) -> int:
        dp = [[0,0] for _ in range(n)]
        dp[0] = [6,6]
        for i in range(1,n):
            dp[i][0] = 3*dp[i-1][0] + 2*dp[i-1][1]
            dp[i][1] = 2*dp[i-1][0] + 2*dp[i-1][1]
        print(dp)
        return dp[-1][0]+dp[-1][1]
    
if __name__ == "__main__":
    s = Solution()
    a1 = 3
    #a2 = 
    print(s.numOfWays(a1))
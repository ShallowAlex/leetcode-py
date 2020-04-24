# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 17:05:19 2020

@author: Alex

code for windows
"""
class Solution:
    def isMatch(self, s, p):
        dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
        dp[-1][-1] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p)-1, -1, -1):
                first_match = i < len(s) and p[j] in {s[i], '?', '*'}
                if p[j] == '*':
                    #print(i,j,first_match)
                    dp[i][j] = dp[i][j+1] or first_match and dp[i+1][j]
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]
        for i in dp:
            print(i)
        return dp[0][0]
    
if __name__ == "__main__":
    s = Solution()
    a1 = "adceb"
    a2 = "*a*b"
    print(s.isMatch(a1, a2))

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 23:50:51 2020
@author: Alex
code for windows
"""
#from typing import List
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        lengh = len(s)
        Max = 10**9+7
        dp = [0] * (lengh+1)
        dp[0] = 1
        for i in range(1,lengh):
            if s[i] == '0':
                continue
            for j in range(10):
                if i + j + 1 >= lengh:
                    break
                if i+j == lengh-2:
                    print(dp)
                if int(s[i:i+j+1]) <= k:
                    dp[i+j] += dp[i-1]
                    if dp[i+j] > Max:
                        dp[i+j] -= Max
                else:
                    break
        print(dp)
        return dp[-1]

    
if __name__ == "__main__":
    s = Solution()
    a1 = '1234567890'
    #a2 = 
    print(s.numberOfArrays(a1,90))
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 22:43:41 2020

@author: Alex

code for windows
"""

class Solution:
    def sortString(self, s: str) -> str:
        from collections import Counter
        ans = ''
        Dict = Counter(s)
        s = set(s)
        s = list(s)
        s.sort()
        flag = 1
        while Dict:
            for i in s[::flag]:
                ans = ans + i
                Dict[i] -= 1
                if Dict[i] == 0:
                    del Dict[i]
            for i in range(len(s))[::-1]:
                if s[i] not in Dict:
                    s.pop(i)
            flag = flag * -1
        return ans
    
    
    
if __name__ == "__main__":
    s = Solution()
    a1 = ""
    #a2 = 
    print(s.sortString(a1))
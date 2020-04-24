# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 11:58:39 2020
@author: Alex
code for windows
"""
#from typing import List
class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        s = {(0,0)}
        count = 0
        while s:
            x, y = s.pop()
            print(x,y,s)
            if x >= m or y >= n:
                continue
            count += 1
            s.update((x+1,y), (x,y+1), (x*10, y), (x,y*10))
        return count
    
if __name__ == "__main__":
    s = Solution()
    #a1 = 
    #a2 = 
    print(s.movingCount(1,2,1))
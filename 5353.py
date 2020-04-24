# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 10:29:09 2020

@author: Alex

code for windows
"""
class Solution:
    def numTimesAllBlue(self, light):
        n = len(light)
        opened = [0]*n
        count = 0
        head = 0
        tail = 0
        for i in range(n):
            if light[i] > tail:
                tail = light[i]
                lengh = tail-head
            
            opened[light[i]-1] = 1
            while head < tail and opened[head] == 1:
                head += 1
                lengh -= 1
            if lengh == 0:
                count += 1
            #print(opened, opened[head:tail], light[i]-1,lengh)
        return count


if __name__ == "__main__":
    s = Solution()
    a1 = [2,1,3,5,4]
    #a2 = 
    print(s.numTimesAllBlue(a1))
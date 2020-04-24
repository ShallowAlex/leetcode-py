# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 22:37:43 2020

@author: Alex

code for windows
"""

class Solution:
    def sortByBits(self, arr):
        def count1(num):
            count = 0
            while num > 0:
                if num & 1 == 1:
                    count += 1
                num = num >> 1
            return count
        tmp = []
        if len(arr) < 2:
            return arr
        flag = 0
        for i in arr:
            if i != 0:
                flag = 1
                break
        if flag == 0:
            return arr
                  
        for i in arr:
            tmp.append(count1(i))
        ans = []
        for i in range(max(tmp)+1):
            tmp1 = []
            for j in range(len(tmp)):
                if tmp[j] == i:
                    tmp1.append(arr[j])
            if tmp1:
                tmp1.sort()
                ans += tmp1
        return ans
    
if __name__ == "__main__":
    s = Solution()
    a1 = [0,1,2,3,4,5,6,7,8]
    #a2 = 
    print(s.sortByBits(a1))
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 16:40:23 2020

@author: Alex

code for windows
"""

class Solution:
    def multiply(self, num1, num2):
        list1 = [int(i) for i in num1[::-1]]
        list2 = [int(i) for i in num2[::-1]]
        l1 = len(num1)
        l2 = len(num2)
        tmp = [0 for i in range(l1+l2)]
        for i in range(l1):
            for j in range(l2):
                num = list1[i] * list2[j]
                tmp[i+j] += num
                print(i,j,tmp)
        ans = ''
        for i in range(l1+l2-2):
            if tmp[i] > 10:
                tmp[i+1] += tmp[i] // 10
                tmp[i] = tmp[i] % 10
        while tmp and tmp[-1] == 0:
            tmp.pop()
        if not tmp:
            return '0'
        for i in tmp[::-1]:
            ans += str(i)
        return ans

if __name__ == "__main__":
    s = Solution()
    a1 = '5'
    a2 = '12'
    print(s.multiply(a1, a2))
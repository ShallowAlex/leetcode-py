# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 11:48:15 2020

@author: Alex

code for windows
"""

class Solution:
    def largestMultipleOfThree(self, digits):
        ans = ''
        digits.sort()
        sum1 = sum(digits)
        div = sum1 % 3
        tmp = []
        if div == 0:
            tmp = digits
        elif div == 1:
            for i in range(len(digits)):
                if digits[i] % 3 == 1:
                    tmp = digits[:i]+digits[i+1:]
                    #print(1,tmp)
                    break
            if not tmp:
                count = []
                n = 2
                for i in range(len(digits)):
                    if digits[i] % 3 == 2:
                        count.append(i)
                        n -= 1
                    if n == 0:
                        tmp = digits[:count[0]]+digits[count[0]+1:count[1]]+digits[count[1]+1:]
                        #print(2,count,tmp)
                        break
        else:
            for i in range(len(digits)):
                if digits[i] % 3 == 2:
                    tmp = digits[:i]+digits[i+1:]
                    #print(3,tmp)
                    break
            if not tmp:
                count = []
                n = 2
                for i in range(len(digits)):
                    if digits[i] % 3 == 1:
                        count.append(i)
                        n -= 1
                    if n == 0:
                        tmp = digits[:count[0]]+digits[count[0]+1:count[1]]+digits[count[1]:]
                        #print(4,tmp)
                        break
        #print(tmp)
        if not tmp:
            return ans
        if tmp[-1] == 0:
            return '0'
        for i in tmp[::-1]:
            ans += str(i)
        return ans

            
if __name__ == "__main__":
    s = Solution()
    a1 = [9,8,1]
    #a2 = 
    print(s.largestMultipleOfThree(a1))
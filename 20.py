# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 15:19:51 2020

@author: Alex

code for windows
"""

class Solution:
    def isValid(self, s: str) -> bool:
        left = ['(', '{', '[']
        right = [')', '}', ']']
        tmp = []
        if s == '':
            return True
        if len(s)%2 == 1:
            return False
        for i in s:
            if i in left:
                tmp.append(i)
            elif i in right:
                if tmp == [] or tmp.pop() != left[right.index(i)]:
                    return False
            else:
                return False
        return tmp == []
    
if __name__ == "__main__":
    s = Solution()
    arr = "){"
    print(s.isValid(arr))
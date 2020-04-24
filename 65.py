# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 16:27:50 2020

@author: Alex

code for windows
"""

import re

class Solution:
    def isNumber(self, s: str) -> bool:
        return bool(re.match(r' *[+-]?([0-9]+(\.[0-9]*)?|\.[0-9]+)(e[+-]?[0-9]+)? *$', s))

if __name__ == "__main__":
    s = Solution()
    a1 = " -90e3   "
    #a2 = 
    print(s.isNumber(a1))

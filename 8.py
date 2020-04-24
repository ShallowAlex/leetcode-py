# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 21:08:41 2020

@author: Alex

code for windows
"""
#import re
#st = re.match(r'^(\s*)([+\-]?)(0*)([0-9]+)', "1095502006p8").groups()
##num = ''.join(re.findall('\d+',st[3]))
#
#print(st)
    

import re
class Solution:
    def myAtoi(self, stri: str) -> int:
        st = re.match(r'^(\s*)([+\-]?)(0*)([0-9]+)', stri)
        if not st:
            return 0
        s = st.groups()
        l = len(str(2**31))
        if len(s[3]) > l:
            if s[1] == '-':
                return -2**31
            else:
                return 2**31-1
        elif len(s[3]) == l:
            if s[1] == '-':
                for i in s[3]:
                    l -= 1
                    if int(i) > (2**31)//(10**l)%10:
                        return -2**31
                    elif int(i) < (2**31)//(10**l)%10:
                        break
                    
            else:
                for i in s[3]:
                    l -= 1
                    if int(i) > (2**31-1)//(10**l)%10:
                        return 2**31-1
                    elif int(i) < (2**31-1)//(10**l)%10:
                        break
        return int(s[1]+s[3])
    
s = Solution()
print(s.myAtoi("2147483646"))
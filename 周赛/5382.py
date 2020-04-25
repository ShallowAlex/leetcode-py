# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 10:14:10 2020
@author: Alex
code for windows
"""
#from typing import List

class Solution:
    def entityParser(self, text: str) -> str:
        dic = {'&quot;':'\"', '&apos;':'\'', '&amp;':'&', '&gt;':'>', '&lt;':'<', '&frasl;':'/'}
        for k in dic.keys():
            if k in text:
                text = text.replace(k, dic[k])
        return text


if __name__ == "__main__":
    s = Solution()
    a1 = "and I quote: &quot;...&quot;"
    #a2 = 
    print(s.entityParser(a1))
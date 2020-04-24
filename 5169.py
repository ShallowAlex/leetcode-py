# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 11:13:03 2020

@author: Alex

code for windows
"""



class Solution:
    def daysBetweenDates(self, date1, date2):
        import datetime
        d1 = datetime.datetime.strptime(date1,"%Y-%m-%d")
        d2 = datetime.datetime.strptime(date2,"%Y-%m-%d")
        return abs((d2-d1).days)
    
if __name__ == "__main__":
    s = Solution()
    a1 = "2020-01-15"
    a2 = "2019-12-31"
    print(s.daysBetweenDates(a1, a2))    
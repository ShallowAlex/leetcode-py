# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 10:53:04 2020

@author: Alex

code for windows
"""

class Solution:
    def rankTeams(self, votes):
        tmp = {}
        for i in votes:
            for index, team in enumerate(i):
                tmp[team] = tmp.get(team, 0) + index
        a = sorted(tmp.items(), key=lambda x: x[1])
        ans = ''
        for i in a:
            ans = ans + i[0]
        return ans
if __name__ == "__main__":
    s = Solution()
    a1 = ["BCA","CAB","CBA","ABC","ACB","BAC"]
    #a2 = 
    print(s.rankTeams(a1))
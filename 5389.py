# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 10:58:13 2020
@author: Alex
code for windows
"""
from typing import List
class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        foods = set()
        for i in orders:
            foods.add(i[2])
        tmp = sorted(list(foods))
        pre = ['table'] + tmp[:]
        dic = {}
        for i in range(len(tmp)):
            dic[tmp[i]] = i
        lengh = len(tmp)
        res = {}
        for _, table, food in orders:
            if table not in res:
                res[table] = [int(table)] + [0]*lengh
            res[table][dic[food]+1] += 1
        ans = []
        for v in res.values():
            ans.append([str(i) for i in v])
        ans.sort(key = lambda i:int(i[0]))
        #print(ans)
        return [pre] + ans
    
if __name__ == "__main__":
    s = Solution()
    a1 = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
    #a2 = 
    print(s.displayTable(a1))
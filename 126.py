# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 14:47:26 2020

@author: Alex

code for windows
"""
from typing import List
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        from collections import defaultdict
        dic = defaultdict(list)
        if endWord not in wordList:
            return []
        ans = []
        begin_visit = {beginWord:[[beginWord]]}
        end_visit = {endWord:[[endWord]]}
        visited = set()
        l = len(beginWord)
        count = 2
        #建立字典
        for w in wordList:
            for i in range(l):
                tmp = w[:i] + '*' + w[i+1:]
                dic[tmp].append(w)
        while begin_visit:
            if len(begin_visit) > len(end_visit):
                begin_visit, end_visit = end_visit, begin_visit
            tmp = {}
            while begin_visit:
                word, path = begin_visit.popitem()
                visited.add(word)
                for i in range(l):
                    tmpword = word[:i] + '*' + word[i+1:]
                    for newword in dic[tmpword]:
                        if newword in end_visit:
                            if path[0][0] == beginWord:
                                ans.extend(p1 + p2[::-1] for p1 in path for p2 in end_visit[newword])
                                print(path, end_visit[newword],'*')
                            else:
                                ans.extend(p2 + p1[::-1] for p1 in path for p2 in end_visit[newword])
                                print(path, end_visit[newword],'$')
                        if newword not in visited:
                            tmp[newword] = tmp.get(newword, []) + [p + [newword] for p in path]
            count += 1
            if ans and len(ans[0]) < count:
                break
            begin_visit = tmp
            #print(begin_visit, end_visit)
        return ans




                
if __name__ == "__main__":
    s = Solution()
    a1 = "a"
    a2 = "c"
    print(s.findLadders(a1, a2, ['a','b','c']))
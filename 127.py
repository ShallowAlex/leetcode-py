# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 14:47:26 2020

@author: Alex

code for windows
"""
from typing import List
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import defaultdict
        dic = defaultdict(list)
        if endWord not in wordList:
            return 0
        begin_visit = {beginWord}
        end_visit = {endWord}
        visited = set()
        l = len(beginWord)
        count = 2
        #建立字典
        for w in wordList:
            for i in range(l):
                tmp = w[:i] + '*' + w[i+1:]
                dic[tmp].append(w)
        flag = 0
        while begin_visit:
            if len(begin_visit) > len(end_visit):
                begin_visit, end_visit = end_visit, begin_visit
            tmp = set()
            while begin_visit:
                word = begin_visit.pop()
                visited.add(word)
                for i in range(l):
                    tmpword = word[:i] + '*' + word[i+1:]
                    for newword in dic[tmpword]:
                        if newword in end_visit:
                            flag = 1
                        if newword not in visited:
                            tmp.add(newword)
            if flag:
                break
            count += 1
            begin_visit = tmp
            print(begin_visit, end_visit)
        return count

                
if __name__ == "__main__":
    s = Solution()
    a1 = "hit"
    a2 = "cog"
    print(s.ladderLength(a1, a2, ["hot","dot","dog","lot","log","cog"]))
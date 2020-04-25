# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 16:57:35 2020

@author: Alex

code for windows
"""

class Solution:
    def findSubstring(self, s, words):
        from collections import Counter
        result = []
        if (not words) or (not s):
            return result
        wordlengh = len(words[0])
        wordcount = len(words)
        end = len(s)
        count_dict = Counter(words)
        for beginword in range(wordlengh):
            tmp = []
            for i in range(beginword, end, wordlengh):
                if i + wordlengh > end + 1:
                    break
                tmp.append(s[i:i+wordlengh])
            begin = 0
            print(tmp)
            while begin + wordcount <= len(tmp):
                countdict = count_dict.copy()
                for i in range(wordcount):
                    if tmp[begin+i] in countdict:
                        #print(begin,i, countdict)
                        countdict[tmp[begin+i]] -= 1
                        if countdict[tmp[begin+i]] == 0:
                            del countdict[tmp[begin+i]]
                    else:
                        break
                if not countdict:
                    result.append(beginword+wordlengh*begin)
                begin += 1
        return result
    
if __name__ == "__main__":
    s = Solution()
    a1 = "barfoothefoobarman"
    a2 = ["foo","bar"]
    print(s.findSubstring(a1, a2))
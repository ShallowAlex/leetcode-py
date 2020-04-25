class Solution:
    def romanToInt(self, s: str) -> int:
        tmp = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        value = 0
        for i in range(len(s)):
            if i+1 < len(s) and tmp[s[i]] < tmp[s[i+1]]:
                value -= tmp[s[i]]
            else:
                value += tmp[s[i]]
        return value
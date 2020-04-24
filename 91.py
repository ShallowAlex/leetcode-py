class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 1 and s != '0':
            return 1
        elif '0' == s[0]:
            return 0
        ans = 1
        a1 = 1
        a2 = 1
        for i in range(1, n):
            if s[i] == '0':
                if s[i-1] <= '2' and s[i-1] != '0':
                    ans = a1
                    a1, a2 = a2, ans
                else:
                    ans = 0
                    break
            else:
                if s[i] <= '6' and s[i-1] == '2' or s[i-1] == '1':
                    ans = a1 + a2
                    a1, a2 = a2, ans
                else:
                    ans = a2
                    a1 = a2
        return ans
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        if m+n != len(s3):
            return False
        ans = [[False]*(n+1) for _ in range(m+1)]
        ans[0][0] = True
        for i in range(1, m+1):
            ans[i][0] = ans[i-1][0] and (s1[i-1] == s3[i-1])
        for j in range(1, n+1):
            ans[0][j] = ans[0][j-1] and (s2[j-1] == s3[j-1])
        for i in range(1, m+1):
            for j in range(1, n+1):
                ans[i][j] = s1[i-1] == s3[i+j-1] and ans[i-1][j] or s2[j-1] == s3[i+j-1] and ans[i][j-1]
        return ans[m][n]
                    
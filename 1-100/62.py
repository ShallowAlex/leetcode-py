class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        tmp = [[0]*m for _ in range(n)]
        tmp[0][0] = 1
        for i in range(n):
            for j in range(m):
                if i > 0:
                    tmp[i][j] += tmp[i-1][j]
                if j > 0:
                    tmp[i][j] += tmp[i][j-1]
        return tmp[n-1][m-1]
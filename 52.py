class Solution:
    def totalNQueens(self, n: int) -> int:
        if n == 0:
            return 0
        ans = 0
        def dfs(row, col, master, slave):
            nonlocal ans
            if row == n:
                ans += 1
            for i in range(n):
                if (i not in col) and (row - i not in master) and (row + i not in slave):
                    dfs(row+1, col|{i}, master|{row-i}, slave|{row+i})
        dfs(0, set(), set(), set())
        return ans
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 0:
            return []
        ans = []
        def dfs(row, col, master, slave, tmp):
            if row == n:
                ans.append(['.' * nums + 'Q' + '.' * (n - nums - 1) for nums in tmp])
            for i in range(n):
                if (i not in col) and (row - i not in master) and (row + i not in slave):
                    dfs(row+1, col|{i}, master|{row-i}, slave|{row+i}, tmp + [i])
        dfs(0, set(), set(), set(), [])
        return ans
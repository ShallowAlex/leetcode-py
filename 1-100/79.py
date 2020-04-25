class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        m = len(board)
        n = len(board[0])
        flag = [[0] * n for _ in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         if board[i][j] == word[0]:
        #             flag[i][j] = 1
        #             if dfs(i, j, word[1:]):
        #                 return True
        #             else:
        #                 flag[i][j] = 0
        
        def dfs(i, j, w):
            if not w:
                return True
            if i < 0 or i > m-1 or j < 0 or j > n-1:
                return False
            if w[0] == board[i][j]:
                if flag[i][j] == 1:
                    return False
                flag[i][j] = 1
                if dfs(i-1, j, w[1:]) or dfs(i+1, j, w[1:]) or dfs(i, j-1, w[1:]) or dfs(i, j+1, w[1:]):
                    return True
                else:
                    flag[i][j] = 0
            return False
        
        for i in range(m):
            for j in range(n):
                if dfs(i, j, word):
                    return True
        return False

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set(range(1,10)) for _ in range(9)]
        col = [set(range(1,10)) for _ in range(9)]
        pool = [set(range(1,10)) for _ in range(9)]
        tmp = []

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    val = int(board[i][j])
                    row[i].remove(val)
                    col[j].remove(val)
                    pool[i//3*3 + j//3].remove(val)
                else:
                    tmp.append((i,j))
        
        def backtrack(index=0):
            if index == len(tmp):
                return True
            i, j = tmp[index]
            num = i//3*3 + j//3
            for val in row[i] & col[j] &pool[num]:
                row[i].remove(val)
                col[j].remove(val)
                pool[num].remove(val)
                if backtrack(index+1):
                    board[i][j] = str(val)
                    return True
                row[i].add(val)
                col[j].add(val)
                pool[num].add(val)
            return False
        backtrack(0)
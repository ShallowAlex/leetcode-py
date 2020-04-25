class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [{} for _ in range(9)]
        col = [{} for _ in range(9)]
        pool = [{} for _ in range(9)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                poolnum = i // 3 * 3 + j // 3
                if board[i][j] != '.':
                    num = int(board[i][j])
                    row[i][num] = row[i].get(num, 0) + 1
                    col[j][num] = col[j].get(num, 0) + 1
                    pool[poolnum][num] = pool[poolnum].get(num, 0) + 1
                    if row[i][num] > 1 or col[j][num] > 1 or pool[poolnum][num] > 1:
                        return False
        return True
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        ans = [[1]]
        for i in range(1, numRows):
            lengh = len(ans[i-1]) + 1
            tmp = [1] * lengh
            for j in range(1, lengh-1):
                tmp[j] = ans[i-1][j-1] + ans[i-1][j]
            ans.append(tmp)
        return ans
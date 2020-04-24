class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if not rowIndex:
            return [1]
        ans = [0] * (rowIndex+1)
        for i in range(rowIndex+1):
            ans[i] = 1
            for j in range(i-1, 0, -1):
                ans[j] += ans[j-1]
        return ans
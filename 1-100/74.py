class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m - 1
        while left < right:
            mid = (left + right + 1) // 2
            if matrix[mid][n-1] > target:
                right = mid - 1
            else:
                left = mid
        if matrix[left][n-1] == target:
            return True
        if left == 0 and matrix[0][n-1] > target:
            row = left
        else:
            row = left + 1
            if row > m - 1:
                return False
        left = 0
        right = n - 1
        while left < right:
            mid = (left +right) // 2
            if matrix[row][mid] < target:
                left =mid + 1
            else:
                right = mid
        return matrix[row][left] == target
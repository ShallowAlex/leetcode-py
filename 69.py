class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        left = 0
        right = x // 2
        while left < right:
            mid = (left + right + 1) // 2
            if mid ** 2 > x:
                right = mid - 1
            else:
                left = mid
        return left
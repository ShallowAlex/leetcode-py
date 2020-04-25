class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxleft = maxright = 0
        ans = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= maxleft:
                    maxleft = height[left]
                else:
                    ans += maxleft - height[left]
                left += 1
            else:
                if height[right] >= maxright:
                    maxright = height[right]
                else:
                    ans += maxright - height[right]
                right -= 1
        return ans
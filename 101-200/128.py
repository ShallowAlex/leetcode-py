class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        for i in nums:  #这里解释一下在set中用in查找的时间复杂度为O(1)
            if i-1 not in nums:
                y = i + 1
                while y in nums:
                    y += 1
                ans = max(ans, y - i)
        return ans
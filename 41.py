class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        if not 1 in nums:
            return 1
        for i in range(n):
            if nums[i] > n or nums[i] < 1:
                nums[i] = 1
        for i in range(n):
            tmp = abs(nums[i])
            nums[tmp] = -abs(nums[tmp])
        for i in range(1,n):
            if nums[i] > 0:
                return i
        return n
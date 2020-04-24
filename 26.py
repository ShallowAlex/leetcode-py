class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums) - 1
        while n > 0:
            if nums[n] == nums[n-1]:
                nums.pop(n)
            n -= 1
        return len(nums)
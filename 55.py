class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr_max = 0
        for index, jump in enumerate(nums):
            if curr_max >= index and index + jump > curr_max:
                curr_max = index + jump
        return curr_max >= len(nums)-1
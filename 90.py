class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = [[]]
        lengh = len(nums)
        tmp = []
        def backtrack(tmp, n):
            for i in range(n, lengh):
                if i > n and nums[i] == nums[i-1]:
                    continue
                tmp.append(nums[i])
                ans.append(tmp[:])
                backtrack(tmp, i+1)
                tmp.pop()
        backtrack(tmp, 0)
        return ans
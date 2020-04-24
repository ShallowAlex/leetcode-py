class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums1, lengh):
            if not nums1:
                result.append(tmp[:])
            for i in range(lengh):
                if i > 0 and nums1[i] == nums1[i-1]:
                    continue
                tmp.append(nums1[i])
                backtrack(nums1[:i]+nums1[i+1:], lengh - 1)
                tmp.pop()
        
        tmp = []
        result = []
        nums.sort()
        lengh = len(nums)
        backtrack(nums, lengh)
        return result
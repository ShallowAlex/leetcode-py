class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if count == 0:
                ans = nums[i]
                print(ans,i)
                count = 1
                continue
            if nums[i] != ans:
                count -= 1
            else:
                count += 1
        print(count)
        return ans
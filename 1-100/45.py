class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        count = 0
        if len(nums) < 2:
            return 0
        while i+nums[i] < len(nums)-1:
            tmpmax = 0
            for j in range(i+1, i+nums[i]+1):
                if nums[j]+j > tmpmax:
                    tmpmax = nums[j]+j
                    tmp = j
            count += 1
            i = tmp
            #print(i, nums[i])
        return count+1
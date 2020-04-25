class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[left] < nums[right]:
                if nums[mid] < target:
                    left = mid + 1
                    #print('*')
                else:
                    right = mid
            elif nums[mid] > nums[left]:
                if nums[mid] >= target and nums[left] <= target:
                    right = mid
                else:
                    left = mid + 1
                    #print('**')
            elif nums[mid] < nums[left]:
                if nums[mid] < target and nums[right] >= target:
                    left = mid + 1
                    #print('***')
                else:
                    right = mid
            else:
                if nums[left] != target:
                    left += 1
                else:
                    break
            #print(left, right)
        return nums[left] == target

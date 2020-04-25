class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        if not nums:
            return -1
        while left < right:
            mid = (left+right)//2
            if nums[left] < nums[right]:
                if target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid
            elif nums[mid] >= nums[left]:
                if target > nums[mid] or target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
            else:
                if target >= nums[left] or target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
        print(left,right)
        if nums[left] == target:
            return left
        return -1
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = []
        for i in nums:
            if not arr or arr[-1] < i:
                arr.append(i)
            if i < arr[-1]:
                l = 0
                r = len(arr)-1
                while l < r:
                    mid = (l+r)//2
                    if arr[mid] < i:
                        l = mid + 1
                    else:
                        r = mid
                arr[l] = i
        print(arr)
        return len(arr)
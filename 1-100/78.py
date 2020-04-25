class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(first):
            print(tmp, first)
            ans.append(tmp[:])
            for i in range(first, n):
                tmp.append(nums[i])
                dfs(i+1)
                tmp.pop()
            
        
        tmp = []
        ans = []
        n = len(nums)
        dfs(0)
        return ans
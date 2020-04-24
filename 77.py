class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(arr, k, first):
            if k == 0:
                #print(arr)
                ans.append(arr[:])
            for i in range(first, n+1):
                arr.append(i)
                dfs(arr, k-1, i+1)
                arr.pop()
        ans = []
        dfs([], k, 1)
        return ans
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        from collections import deque
        arr = deque()
        sums = 0
        ans = []
        for i in range(1,(target+1)//2 + 1):
            if sums < target:
                arr.append(i)
                sums += i
            while sums > target:
                sums -= arr.popleft()
            if sums == target:
                ans.append(list(arr))
                sums -= arr.popleft()
        return ans
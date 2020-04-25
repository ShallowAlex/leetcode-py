class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        top = 1
        bottom = 0
        ans = 0
        p = 1
        lengh = len(prices)
        while p < lengh:
            while p < lengh and prices[p] <= prices[p-1]:
                p += 1
            bottom = p - 1
            while p < lengh and prices[p] > prices[p-1]:
                p += 1
            top = p - 1
            ans += prices[top] - prices[bottom]
        return ans

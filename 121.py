class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        bottom = 0
        top = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[bottom]:
                bottom = i
                top = i
            if prices[i] > prices[top]:
                top = i
                ans = max(ans, prices[top]-prices[bottom])
        return ans
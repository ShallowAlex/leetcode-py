class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lengh = len(prices)
        if lengh < 2:
            return 0
        
        dp = [[float('-inf')]*5 for _ in range(lengh)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(lengh):
            dp[i][3] = float('-inf')
        for i in range(1, lengh):
            dp[i][0] = 0
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i])
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
            dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i])
        print(*dp, sep = '\n')
        return max(0, dp[lengh-1][2], dp[lengh-1][4])
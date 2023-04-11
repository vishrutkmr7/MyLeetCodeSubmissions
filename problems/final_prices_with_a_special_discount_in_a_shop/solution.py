class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        dp = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                if prices[j] <= prices[i]:
                    dp[i] = prices[i] - prices[j]
                    break
            else:
                dp[i] = prices[i]
        return dp
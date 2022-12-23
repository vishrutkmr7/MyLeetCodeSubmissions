class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0

        buy = [0] * len(prices)
        sell = [0] * len(prices)
        cooldown = [0] * len(prices)

        buy[0] = -prices[0]
        buy[1] = max(-prices[0], -prices[1])
        sell[1] = max(0, prices[1] - prices[0])
        cooldown[1] = 0

        for i in range(2, len(prices)):
            buy[i] = max(buy[i - 1], cooldown[i - 1] - prices[i])
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
            cooldown[i] = max(cooldown[i - 1], sell[i - 1])

        return sell[-1]
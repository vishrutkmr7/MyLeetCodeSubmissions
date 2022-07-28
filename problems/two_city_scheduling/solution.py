class Solution:
    def twoCitySchedCost(self, prices: List[List[int]]) -> int:
        prices.sort(key=lambda x: x[1] - x[0])
        return sum(
            cost[1] if i < len(prices) / 2 else cost[0] for i, cost in enumerate(prices)
        )
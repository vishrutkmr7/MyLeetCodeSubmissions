class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        @cache
        def dp(i, t):
            if i == len(cost):
                return 0 if t >= 0 else inf
            return min(dp(i + 1, t - 1), cost[i] + dp(i + 1, min(t + time[i], len(cost))))
        return dp(0, 0)
        
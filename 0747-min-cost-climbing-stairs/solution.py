class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        steps = len(cost)
        if steps < 2: return cost[steps]
        cost1 = cost[0]
        cost2 = cost[1]
        for i in range(2, steps):
            temp = cost[i] + min(cost1, cost2)
            cost1 = cost2
            cost2 = temp
        
        return min(cost1, cost2)

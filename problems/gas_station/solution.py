class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_gas = 0
        start = 0
        remaining = 0
        for i in range(n):
            total_gas += gas[i] - cost[i]
            remaining += gas[i] - cost[i]
            if remaining < 0:
                start = i + 1
                remaining = 0
        
        return start if total_gas >= 0 else -1
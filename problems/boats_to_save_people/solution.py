class Solution:
    def numRescueBoats(self, weights: List[int], limit: int) -> int:
        weights.sort()
        lo = 0
        hi = len(weights) - 1
        boats = 0
        while lo <= hi:
            if weights[lo] + weights[hi] <= limit:
                lo += 1
            hi -= 1
            boats += 1
        return boats
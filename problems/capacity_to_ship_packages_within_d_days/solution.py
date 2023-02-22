class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship(weights, days, capacity):
            d = 1
            w = 0
            for weight in weights:
                if w + weight > capacity:
                    d += 1
                    w = 0
                w += weight
            return d <= days

        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = (left + right) // 2
            if can_ship(weights, days, mid):
                right = mid
            else:
                left = mid + 1
        return left
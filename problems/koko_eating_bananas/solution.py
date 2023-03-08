class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(piles: list[int], h: int, k: int) -> bool:
            """
            Returns True if Koko can finish eating all the bananas within h hours.
            """
            hours = 0
            for pile in piles:
                hours += pile // k
                if pile % k != 0:
                    hours += 1
            return hours <= h

        # Binary search for the minimum k
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if canFinish(piles, h, mid):
                right = mid
            else:
                left = mid + 1
        return left
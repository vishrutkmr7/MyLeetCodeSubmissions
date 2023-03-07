class Solution:
    def minimumTime(self, time: list[int], totalTrips: int) -> int:
        low, high = 1, totalTrips * min(time)

        while low < high:
            mid = (low + high) // 2
            if sum(mid // t for t in time) < totalTrips:
                low = mid + 1
            else:
                high = mid

        return low

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        starts = [x for x, y, z in events]
        
        @lru_cache(None)
        def dp(idx, k):
            if k == 0 or idx >= len(events):
                return 0
            next_event = bisect_right(starts, events[idx][1])
            return max(dp(idx+1, k), events[idx][2] + dp(next_event, k - 1))
    
        return dp(0, k)
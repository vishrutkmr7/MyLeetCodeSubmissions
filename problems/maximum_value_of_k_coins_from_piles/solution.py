class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @lru_cache(None)
        def dp(i, k):
            if k == 0 or i == len(piles): return 0
            res, cur = dp(i + 1, k), 0
            for j in range(min(len(piles[i]), k)):
                cur += piles[i][j]
                res = max(res, cur + dp(i+1, k-j-1))
            return res
        
        return dp(0, k)
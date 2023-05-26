class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        for i in range(N - 2, -1, -1):
            piles[i] += piles[i + 1]

        @lru_cache(None)
        def dp(i, m):
            if i + 2 * m >= N:
                return piles[i]
            return piles[i] - min(dp(i + x, max(m, x)) for x in range(1, 2 * m + 1))

        return dp(0, 1)
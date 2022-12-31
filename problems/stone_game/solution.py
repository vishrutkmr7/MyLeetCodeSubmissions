class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        length = len(piles)

        dp = [[0] * length for _ in range(length)]

        for i in range(length):
            dp[i][i] = piles[i]

        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1])

        return dp[0][length - 1] > 0
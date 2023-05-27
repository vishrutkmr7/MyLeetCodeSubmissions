class Solution:
    def cmp(self, a, b):
        return (a > b) - (a < b)

    def stoneGameIII(self, A: list[int]) -> str:
        dp = [0] * 3
        for i in range(len(A) - 1, -1, -1):
            dp[i % 3] = max(sum(A[i : i + k]) - dp[(i + k) % 3] for k in (1, 2, 3))
        return ["Tie", "Alice", "Bob"][self.cmp(dp[0], 0)]

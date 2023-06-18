class Solution:
    def countPaths(self, grid: list[list[int]]) -> int:
        m, n, mod = len(grid), len(grid[0]), 10**9 + 7
        dp = [[1] * n for _ in range(m)]
        for _, i, j in sorted([grid[i][j], i, j] for i in range(m) for j in range(n)):
            for x, y in [[i, j + 1], [i, j - 1], [i + 1, j], [i - 1, j]]:
                if 0 <= x < m and 0 <= y < n and grid[x][y] < grid[i][j]:
                    dp[i][j] += dp[x][y] % mod
        return sum(map(sum, dp)) % mod

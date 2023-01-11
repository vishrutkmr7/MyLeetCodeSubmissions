class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        res = (1 << col - 1) * row
        for j in range(1, col):
            cur = sum(grid[i][j] == grid[i][0] for i in range(row))
            res += max(cur, row - cur) * (1 << col - 1 - j)
        return res
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                r < 0
                or r >= row
                or c < 0
                or c >= col
                or grid[r][c] == 0
                or grid[r][c] == "#"
            ):
                return 0
            temp = grid[r][c]
            grid[r][c] = "#"
            point = max(
                dfs(r + 1, c) + temp,
                dfs(r - 1, c) + temp,
                dfs(r, c + 1) + temp,
                dfs(r, c - 1) + temp,
            )

            grid[r][c] = temp

            return point

        point = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 0:
                    continue
                point = max(dfs(r, c), point)

        return point
        

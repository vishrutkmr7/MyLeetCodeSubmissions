class Solution(object):
    def maxAreaOfIsland(self, grid):
        def dfs(i: int, j: int) -> int:
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                grid[i][j] = 0
                return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
            return 0

        max_area = 0
        for index, _ in enumerate(grid):
            for j in range(len(grid[0])):
                if grid[index][j] == 1:
                    max_area = max(max_area, dfs(index, j))
        return max_area

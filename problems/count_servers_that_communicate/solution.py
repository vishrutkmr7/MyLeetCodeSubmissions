class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        count = 0
        rows_with_servers = [0] * len(grid)
        cols_with_servers = [0] * len(grid[0])
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    rows_with_servers[row] += 1
                    cols_with_servers[col] += 1

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (
                    rows_with_servers[row] > 1 or cols_with_servers[col] > 1
                ):
                    count += 1
        return count

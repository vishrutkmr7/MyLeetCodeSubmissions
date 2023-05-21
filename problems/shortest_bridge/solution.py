class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        found = False
        stack = []
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    self.dfs(grid, i, j, n, m, stack)
                    found = True
                    break
            if found:
                break
        steps = 0
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while stack:
            size = len(stack)
            level = []
            while size:
                temp = stack.pop()
                size -= 1
                x, y = temp[0], temp[1]
                for dx, dy in dirs:
                    tx = x + dx
                    ty = y + dy
                    if tx < 0 or ty < 0 or tx >= n or ty >= m or grid[tx][ty] == 2:
                        continue
                    if grid[tx][ty] == 1:
                        return steps
                    grid[tx][ty] = 2
                    level.append((tx, ty))
            steps += 1
            stack = level
        return -1

    def dfs(self, grid, row, col, n, m, stack):
        if row < 0 or col < 0 or row >= n or col >= m or grid[row][col] != 1:
            return
        grid[row][col] = 2
        stack.append((row, col))
        self.dfs(grid, row + 1, col, n, m, stack)
        self.dfs(grid, row - 1, col, n, m, stack)
        self.dfs(grid, row, col + 1, n, m, stack)
        self.dfs(grid, row, col - 1, n, m, stack)

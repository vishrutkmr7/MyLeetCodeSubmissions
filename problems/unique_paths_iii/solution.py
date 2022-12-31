class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.count = 0
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        self.empty = 1
        for i, j in itertools.product(range(self.m), range(self.n)):
            if grid[i][j] == 1:
                self.start = (i, j)
            elif grid[i][j] == 2:
                self.end = (i, j)
            elif grid[i][j] == 0:
                self.empty += 1
        self.dfs(self.start[0], self.start[1], 0)
        return self.count

    def dfs(self, i, j, visited):
        if i < 0 or j < 0 or i >= self.m or j >= self.n or self.grid[i][j] == -1:
            return
        if self.grid[i][j] == 2:
            if visited == self.empty:
                self.count += 1
            return
        self.grid[i][j] = -1
        self.dfs(i + 1, j, visited + 1)
        self.dfs(i - 1, j, visited + 1)
        self.dfs(i, j + 1, visited + 1)
        self.dfs(i, j - 1, visited + 1)
        self.grid[i][j] = 0

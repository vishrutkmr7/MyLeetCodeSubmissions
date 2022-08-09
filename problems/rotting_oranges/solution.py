class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = []
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        time = 0
        fresh = 0
        vis = [[True] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append([i, j])
                elif grid[i][j] == 1:
                    fresh += 1
        while q:
            for _ in range(len(q)):
                x, y = q.pop(0)
                for k in range(4):
                    if (
                        x + dx[k] > -1
                        and x + dx[k] < m
                        and y + dy[k] > -1
                        and y + dy[k] < n
                        and grid[x + dx[k]][y + dy[k]] == 1
                    ):
                        grid[x + dx[k]][y + dy[k]] = 2
                        q.append([x + dx[k], y + dy[k]])
                        fresh -= 1
            if q:
                time += 1
        return time if fresh == 0 else -1
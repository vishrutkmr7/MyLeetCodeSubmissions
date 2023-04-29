class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        m, n = len(grid), len(grid[0])
        q = deque([(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1])
        if len(q) in [0, m * n]:
            return -1
        level = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    new_i, new_j = i + x, j + y
                    if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == 0:
                        grid[new_i][new_j] = 1
                        q.append((new_i, new_j))
            level += 1
        return level - 1
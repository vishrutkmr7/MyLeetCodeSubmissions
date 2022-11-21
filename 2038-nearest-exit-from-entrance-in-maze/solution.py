class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        queue = deque()
        queue.append((entrance[0], entrance[1]))
        maze[entrance[0]][entrance[1]] = "+"
        steps = 0
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if (row == 0 or row == m - 1 or col == 0 or col == n - 1) and (
                    row,
                    col,
                ) != (entrance[0], entrance[1]):
                    return steps
                for r, c in [
                    (row + 1, col),
                    (row - 1, col),
                    (row, col + 1),
                    (row, col - 1),
                ]:
                    if 0 <= r < m and 0 <= c < n and maze[r][c] == ".":
                        queue.append((r, c))
                        maze[r][c] = "+"
            steps += 1
        return -1
